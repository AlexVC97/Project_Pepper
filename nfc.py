#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
from time import sleep
from threading import Thread
import logging
import logging.handlers
from config_handler import ConfigHandler
import json
import datetime

class Nfc(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.my_mqtt = client
        self.configHandler = ConfigHandler()
        self.data = {"uid": [0,0,0,0,0], "pkt_ctr": 0}

    def run(self):
        continue_reading = True
        oldUid = [0,0,0,0,0]

        self.configHandler.read_json()
        pkt_ctr = 1

        # Create an object of the class MFRC522
        MIFAREReader = MFRC522.MFRC522()

        # Welcome message
        print "Identificatie APP"
        print "Press break to stop."

        MIFAREReader.Write_MFRC522(0x04,0x55)

        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while continue_reading:
            # Scan for cards
            (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            #sleep(1)
            # If a card is found
            if status == MIFAREReader.MI_OK:
                #print "Card detected"
                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()

                # If we have the UID, continue
                if status == MIFAREReader.MI_OK:
                    if oldUid != uid:
                        oldUid = uid
                        current_date = datetime.datetime.now()
                        epoch = int(current_date.strftime("%s"))
                        print "Read: " + str(uid)
                        logging.info("nfc:Card read UID: " + str(uid))
                        self.data['pkt_ctr'] = pkt_ctr
                        self.data['uid'] = str(uid)
                        self.data['timestamp'] = epoch
                        json_data = json.dumps(self.data)
                        try:
                            self.my_mqtt.publishing(self.configHandler.get_nfcTopic(), json_data)
                        except Exception:
                            logging.warning("nfc:Couldn't publish the data!")
                        pkt_ctr += 1

#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
from backend import Backend
from time import sleep
from threading import Thread
import logging
import logging.handlers
from config_handler import ConfigHandler
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("logging.pepper.out")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Nfc(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.my_mqtt = client
        self.configHandler = ConfigHandler()
        self.data = {"card_id": 0, "uid": [0,0,0,0,0]}

    def run(self):
        continue_reading = True
        oldUid = [0,0,0,0,0]

        self.configHandler.read_json()
        card_id = 0

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

            sleep(1)
            # If a card is found
            if status == MIFAREReader.MI_OK:
                #print "Card detected"
                # Get the UID of the card
                (status,uid) = MIFAREReader.MFRC522_Anticoll()

                # If we have the UID, continue
                if status == MIFAREReader.MI_OK:
                    #Print UID
                    #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4])

                    flag_read = True
                    if oldUid != uid:
                        oldUid = uid
                        print "Read: " + str(uid)
                        logger.info("Card read UID: " + str(uid))
                        self.data['card_id'] = card_id
                        self.data['uid'] = str(uid)
                        self.data['timestamp'] = str(datetime.now())
                        json_data = json.dumps(self.data)
                        self.my_mqtt.publishing(self.configHandler.get_nfcTopic(), json_data)
                        card_id += 1
                        # This is the default key for authentication
                        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

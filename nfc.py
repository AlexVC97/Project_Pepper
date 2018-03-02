#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
from time import sleep
from threading import Thread
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("logging.pepper.out")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Nfc(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.continue_reading = True
        self.uid = [0,0,0,0,0]
        # Create an object of the class MFRC522
        self.MIFAREReader = MFRC522.MFRC522()

    def set_uid(self):
        # Get the UID of the card
        (status,self.uid) = self.MIFAREReader.MFRC522_Anticoll()

    def get_uid(self):
        return str(self.uid)

    def run(self):
        oldUid = [0,0,0,0,0]

        # Welcome message
        print "Identificatie APP"
        print "Press break to stop."

        self.MIFAREReader.Write_MFRC522(0x04,0x55)

        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while self.continue_reading:
            # Scan for cards
            (status,TagType) = self.MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            sleep(1)
            # If a card is found
            if status == self.MIFAREReader.MI_OK:
                #print "Card detected"
                Nfc().set_uid()

                # If we have the UID, continue
                if status == self.MIFAREReader.MI_OK:
                    #Print UID
                    #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4])

                    flag_read = True
                    if oldUid != uid:
                        oldUid = uid
                        logger.debug("Card read UID: " + str(uid))
                       # This is the default key for authentication
                        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
from time import sleep
from threading import Thread

class Nfc(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.continue_reading = True

    def run(self):
        oldUid = [0,0,0,0,0]

        # Create an object of the class MFRC522
        MIFAREReader = MFRC522.MFRC522()

        # Welcome message
        print "Identificatie APP"
        print "Press Ctrl-C to stop."

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
                    # Print UID
                    #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

                    flag_read = True
                    #print str(uid)
                    if oldUid != uid:
                       oldUid = uid
                       if (uid == [138,201,99,6,38]):
                         print "Welkom Kurt"
                       elif (uid == [4,7,107,1,105]):
                         print "Welkom Lucas"
                       elif (uid == [6,204,246,147,175]):
                         print "Welkom Emma"
                       elif (uid == [168,151,17,4,42]):
                         print "Welkom Christophe"
                       else:
                         print "onbekende persoon"
                       # This is the default key for authentication
                       key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

                       # Select the scanned tag
                       #MIFAREReader.MFRC522_SelectTag(uid)

                       # Authenticate
                       #status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

                       # Check if authenticated
                       #if status == MIFAREReader.MI_OK:
                       #    MIFAREReader.MFRC522_Read(8)
                       #    MIFAREReader.MFRC522_StopCrypto1()
                       #else:
                       #    print "Authentication error"

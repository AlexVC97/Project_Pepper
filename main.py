#!/usr/bin/env python

from autobahn.twisted.wamp import ApplicationRunner
from os import environ
from broadcast import Broadcast
from nfc import Nfc
from backend import Backend
from time import *
import json
import logging
import logging.handlers

hostSerialNo = ""
nfc = False

with open('config.json') as json_data:
    data = json.load(json_data)
    hostSerialNo = data['HostSerialNo']
    nfc = data['NFC']

def main():
    logging.getLogger(__name__)
    logging.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    rotate_handler = logging.handlers.RotatingFileHandler('logging.pepper.out', mode='a', maxBytes=1024000, backupCount=2)
    rotate_handler.doRollover()
    rotate_handler.setFormatter(formatter)
    logging.addHandler(rotate_handler)

if __name__ == "__main__":
    main()
    print hostSerialNo
    print nfc

    broadcast = Broadcast(hostSerialNo)
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    if(nfc == True):
        nfcThread.start()
        nfcThread.join()

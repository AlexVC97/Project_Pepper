#!/usr/bin/env python

from autobahn.twisted.wamp import ApplicationRunner
from os import environ
from broadcast import Broadcast
from nfc import Nfc
from backend import Backend
from time import *
import json

hostSerialNo = ""
nfc = False

with open('config.json') as json_data:
    data = json.load(json_data)
    hostSerialNo = data['HostSerialNo']
    nfc = data['NFC']

if __name__ == "__main__":
    broadcast = Broadcast(serialNo)
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    if(nfc == True):
        nfcThread.start()
        nfcThread.join()

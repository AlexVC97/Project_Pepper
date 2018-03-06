#!/usr/bin/env python

from broadcast import Broadcast
from nfc import Nfc
from time import *
#from publish import Publish
#import paho.mqtt.client as mqtt
import json

hostSerialNo = ""
nfc = False

with open('config.json') as json_data:
    data = json.load(json_data)
    hostSerialNo = data['HostSerialNo']
    nfc = data['NFC']

def main():
    broadcast = Broadcast(hostSerialNo)
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    if(nfc == True):
        nfcThread.start()
        nfcThread.join()

if __name__ == "__main__":
    main()

    print ip[0]

#!/usr/bin/env python

from broadcast import Broadcast
from nfc import Nfc
from time import *
from client_handler import ClientHandler
import json

hostSerialNo = ""
nfc = False
port = 1883

with open('config.json') as json_data:
    data = json.load(json_data)
    hostSerialNo = data['HostSerialNo']
    nfc = data['NFC']

def main():
    broadcast = Broadcast(hostSerialNo)

    broadcast.config_socket()
    broadcast.send_broadcast()

    mqtt_client = ClientHandler(broadcast.ip[0], port)
    mqtt_client.make_connection()

    nfcThread = Nfc(mqtt_client)

    if(nfc == True):
        nfcThread.start()
        nfcThread.join()

if __name__ == "__main__":
    main()

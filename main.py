#!/usr/bin/env python3

from broadcast import Broadcast
from nfc import Nfc
from time import *
import json

with open('config.json') as json_data:
    data = json.load(json_data)
    serialNo = data['SerialNo']
    nfc = data['NFC']

if __name__ == "__main__":
    broadcast = Broadcast(serialNo)
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    if(nfc == True):
        nfcThread.start()
        nfcThread.join()

    '''
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://192.168.1.192:8080/ws"),
        u"crossbardemo",
    )
    runner.run(Backend)
    '''

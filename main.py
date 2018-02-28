from broadcast import Broadcast
from nfc import Nfc
from time import *
import json

serialNo = ""

with open('config.json') as json_data:
    data = json.load(json_data)
    serialNo = data['SerialNo']
    rfid = data['RFID']

if __name__ == "__main__":
    broadcast = Broadcast(serialNo)
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    nfcThread.start()
    nfcThread.join()

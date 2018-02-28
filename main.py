from broadcast import Broadcast
from nfc import Nfc
from time import *
import json
SerialNo = ""
with open('config.json') as json_data:
    data = json.load(json_data)
    SerialNo = data['SerialNo']
    print data['RFID']

if __name__ == "__main__":
    print SerialNo
    broadcast = Broadcast("1254268ECHDN")
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    nfcThread.start()
    nfcThread.join()

from broadcast import Broadcast
from nfc import Nfc
from time import *
import json

with open('config.json') as json_data:
    data = json.load(json_data)
    print data['Pepper']['SerialNo']
    for config in data['Pepper']:
        print config['SerialNo']

if __name__ == "__main__":
    broadcast = Broadcast("1254268ECHDN")
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    nfcThread.start()
    nfcThread.join()

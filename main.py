from broadcast import Broadcast
from nfc import Nfc
from time import *

if __name__ == "__main__":
    broadcast = Broadcast("1254268ECHDN")
    nfcThread = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    nfcThread.start()
    nfcThread.join()

from broadcast import Broadcast
from nfc import Nfc
from time import *

if __name__ == "__main__":
    broadcast = Broadcast("1254268ECHDN")
    myThreadOb1 = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    myThreadOb1.start()
    myThreadOb1.join()

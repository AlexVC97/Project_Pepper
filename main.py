from rpi_broadcast import *
from nfc import Nfc
from time import *

if __name__ == "__main__":
    broadcast = RpiBroadcast("1254268ECHDN")
    myThreadOb1 = Nfc()

    broadcast.config_socket()
    broadcast.send_broadcast()

    myThreadOb1.start()
    myThreadOb1.join()

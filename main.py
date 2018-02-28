from rpi_broadcast import RpiBroadcast
from nfc import Nfc

if __name__ == "__main__":
    broadcast = RpiBroadcast("1254268ECHDN")
    myThreadOb1 = Nfc()

    broadcast.send_broadcast()

    myThreadOb1.start()
    myThreadOb1.join()

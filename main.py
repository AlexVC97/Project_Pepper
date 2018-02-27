#from rpi_broadcast import RpiBroadcast
from nfc import Nfc

if __name__ == "__main__":
    #myThreadOb1 = RpiBroadcast("1254268ECHDN")
    myThreadOb2 = Nfc()

    #myThreadOb1.start()
    myThreadOb2.start()

    #myThreadOb1.join()
    myThreadOb2.join()

#from rpi_broadcast import RpiBroadcast
from nfc import Nfc
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    #global continue_reading
    print "Ctrl+C captured, ending read."
    myThreadOb2.continue_reading = False
    GPIO.cleanup()

if __name__ == "__main__":
    #myThreadOb1 = RpiBroadcast("1254268ECHDN")
    myThreadOb2 = Nfc()

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    #myThreadOb1.start()
    myThreadOb2.start()

    #myThreadOb1.join()
    myThreadOb2.join()

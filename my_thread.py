from threading import Thread
from random import randint
import time

class MyThread(Thread):
    def __init__(self, val):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self.val = val

    def run(self):
        for i in range(1, self.val):
            print("Value %d in thread %s" % (i, self.getName()))

            # Sleep for random time between 1 ~ 3 second
            secondsToSleep = randint(1, 5)
            print("%s sleeping for %d seconds..." % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)

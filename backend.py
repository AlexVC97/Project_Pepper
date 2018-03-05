#!/usr/bin/env python

from __future__ import print_function
from os import environ
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession

class Backend(ApplicationSession):
    '''
    An application component that publishes an event every second.
    '''

    @inlineCallbacks
    def onJoin(self, details):
        counter = 0
        while True:
            print("publish: com.myapp.topic1", counter)
            self.publish(u'com.myapp.topic1', counter)

            print("publish: com.myapp.topic2 'Hello world.'")
            self.publish(u'com.myapp.topic2', "Hello world.")
            counter += 1
            yield sleep(1)

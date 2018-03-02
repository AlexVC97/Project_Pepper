#!/usr/bin/env python3

from os import environ
import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class Backend(ApplicationSession):
    '''
    An application component that publishes an event every second.
    '''

    async def onJoin(self, details):
        counter = 0
        while True:
            print("publish: com.myapp.topic1", counter)
            self.publish(u'com.myapp.topic1', counter)

            print("publish: com.myapp.topic2 'Hello world.'")
            self.publish(u'com.myapp.topic2', "Hello world.")
            counter += 1
            await asyncio.sleep(1)

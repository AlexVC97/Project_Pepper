#!/usr/bin/env python3

from os import environ
import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class Component(ApplicationSession):
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

if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://192.168.1.192:8080/ws"),
        u"crossbardemo",
    )
    runner.run(Component)

import paho.mqtt.client as mqtt
import time
import logging

class Publish():
    def __init__(self, broker_address):
        self.broker_address = broker_address

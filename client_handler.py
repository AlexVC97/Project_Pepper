from communication import Communication
import paho.mqtt.client as mqtt
from time import *
import logging

class ClientHandler():
    def __init__(self, broker_ip, broker_port):
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.communication = Communication()
        self.client = mqtt.Client("PUB_CLIENT") # Create new instance

    def make_connection(self):
        mqtt.Client.connected_flag = False # Create flag in class
        self.client.on_connect = self.communication.on_connect
        self.client.on_disconnect = self.communication.on_disconnect
        self.client.on_publish = self.communication.on_publish
        try:
            self.client.connect(self.broker_ip, self.broker_port) # Establish connection
        except Exception as exception:
            print "Connection can't be established with " + self.broker_ip
            logging.warning("clienthandler:Connection can't be established with " + self.broker_ip)
        self.client.loop_start()
        logging.info("clienthandler:Waiting for connection..")
        while not self.client.connected_flag: # Wait in loop
            print "Waiting for connection.."
            sleep(1)
        sleep(3)

    def publishing(self, topic, msg):
        ret = self.client.publish(topic, msg, 0) # Publish
        print "Published return = " + str(ret)
        sleep(3)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

#!/usr/bin/env python

from broadcast import Broadcast
from nfc import Nfc
from time import *
from client_handler import ClientHandler
from config_handler import ConfigHandler
import logging

logging.basicConfig(level = logging.INFO,
    format = "%(asctime)s:%(levelname)s:%(message)s")
logging.handlers.RotatingFileHandler('logging.pepper.out', mode='a', maxBytes=1024000, backupCount=2)

def main():
    configHandler = ConfigHandler()
    configHandler.read_json()

    broadcast = Broadcast(configHandler.get_hostSerialNo())
    broadcast.config_socket()
    broadcast.send_broadcast()

    mqtt_client = ClientHandler(configHandler.get_mqttBroker(),
        configHandler.get_mqttPort())
    mqtt_client.make_connection()

    nfcThread = Nfc(mqtt_client)

    if(configHandler.get_nfc() == True):
        nfcThread.start()
        nfcThread.join()

if __name__ == "__main__":
    main()

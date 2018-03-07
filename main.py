#!/usr/bin/env python

from broadcast import Broadcast
from nfc import Nfc
from time import *
from client_handler import ClientHandler
from config_handler import ConfigHandler

def main():
    configHandler = ConfigHandler()
    configHandler.read_json()

    broadcast = Broadcast(configHandler.get_hostSerialNo())
    print "SERIALNO: " + configHandler.get_hostSerialNo()
    broadcast.config_socket()
    broadcast.send_broadcast()

    mqtt_client = ClientHandler(configHandler.get_mqttBroker(),
        configHandler.get_mqttPort())
    print "BROKER: " + configHandler.get_mqttBroker()
    print "PORT: " + str(configHandler.get_mqttPort())
    mqtt_client.make_connection()

    nfcThread = Nfc(mqtt_client)

    print "NFC: " + configHandler.get_nfc()

    if(configHandler.get_nfc() == True):
        nfcThread.start()
        nfcThread.join()

if __name__ == "__main__":
    main()

#!/usr/bin/env python

from socket import *
from time import *
import re
import logging
#import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Broadcast():
    def __init__(self, serialNo):
        self.serialNo = serialNo
        self.data = ""
        self.address = ("", 5001)
        self.validIpAddressRegex = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
        self.udpSocket = socket(AF_INET, SOCK_DGRAM)

    def config_socket(self):
        # Indicates if the local address can be reused
        self.udpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # Set TTL in the IP header
        self.udpSocket.setsockopt(SOL_IP, IP_TTL, 1)
        # Enable the socket for issuing messages to a broadcast address
        self.udpSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.udpSocket.bind(self.address)
        self.udpSocket.settimeout(1)
        print "Socket has been configured, waiting for the IP address.."
        logger.debug("Socket has been configured, waiting for the IP address..")

    def send_broadcast(self):
        while(self.data != "true"):
            try:
                self.udpSocket.sendto(self.serialNo, ("<broadcast>", 5000))
                self.data, addr = self.udpSocket.recvfrom(1024) # 1 kilo Byte
            except error:
                self.data = None
            if self.data is None:
                logger.debug("Nothing received yet! Try again!")
        convert = "".join(map(str,addr))
        ip = re.findall(self.validIpAddressRegex, convert)
        print "Received: " + ip[0]
        logger.debug("Received: " + ip[0])
        sleep(5)

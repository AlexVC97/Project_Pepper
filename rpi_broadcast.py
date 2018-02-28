from socket import *
import re
from time import *

class RpiBroadcast():
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

    def send_broadcast(self):
        while(self.data != "true"):
            try:
                self.udpSocket.settimeout(1)
                print self.data
                self.udpSocket.sendto(self.serialNo, ("<broadcast>", 5000))
                self.data, addr = UDPSocket.recvfrom(1024) # 1 kilo Byte
            except error:
                self.data = None
            if self.data is None:
                print "Nothing received yet! Try again!"
        print self.data
        convert = "".join(map(str,addr))
        ip = re.findall(self.validIpAddressRegex, convert)
        print ip[0]
        sleep(5)

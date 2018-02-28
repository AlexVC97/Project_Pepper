from socket import *
import re
from time import *

class RpiBroadcast():
    def __init__(self, serialNo):
        self.serialNo = serialNo
        self.data = ""
        self.address = ("", 5001)
        self.validIpAddressRegex = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'

    @staticmethod
    def create_socket():
        UDPSocket = socket(AF_INET, SOCK_DGRAM)
        # Indicates if the local address can be reused
        UDPSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # Set TTL in the IP header
        UDPSocket.setsockopt(SOL_IP, IP_TTL, 1)
        # Enable the socket for issuing messages to a broadcast address
        UDPSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDPSocket.bind(address)
        UDPSocket.settimeout(1)

    def send_broadcast(self):
        while(self.data != "true"):
            try:
                print self.data
                UDPSocket.sendto(self.serialNo, ("<broadcast>", 5000))
                self.data, addr = UDPSocket.recvfrom(1024) # 1 kilo Byte
            except error:
                data = None
            if data is None:
                print "Nothing received yet! Try again!"
        print self.data
        convert = "".join(map(str,addr))
        ip = re.findall(self.validIpAddressRegex, convert)
        print ip[0]
        sleep(5)

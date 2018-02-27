from socket import *
import re
from time import *
from threading import Thread

class RpiBroadcast(Thread):
    def __init__(self, serialNo):
        Thread.__init__(self)
        self.serialNo = serialNo

    def run(self):
        address = ("", 5001)
        data = "false"
        validIpAddressRegex = r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})'
        UDPSocket = socket(AF_INET, SOCK_DGRAM)
        # Indicates if the local address can be reused
        UDPSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # Set TTL in the IP header
        UDPSocket.setsockopt(SOL_IP, IP_TTL, 1)
        # Enable the socket for issuing messages to a broadcast address
        UDPSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDPSocket.bind(address)
        UDPSocket.settimeout(1)
        while(data != "true"):
            try:
                print data
                UDPSocket.sendto(self.serialNo, ("<broadcast>", 5000))
                data, addr = UDPSocket.recvfrom(1024) # 1 kilo Byte
            except error:
                data = None
            if data is None:
                print "Nothing received yet! Try again!"
        print data
        convert = "".join(map(str,addr))
        ip = re.findall(validIpAddressRegex, convert)
        print ip[0]
        sleep(5)

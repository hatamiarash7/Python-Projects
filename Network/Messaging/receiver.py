import os
from socket import *

HOST = ''
PORT = 80
Address = (HOST, PORT)
BUFFER = 1024
UDPSocket = socket(AF_INET, SOCK_DGRAM)
UDPSocket.bind(Address)
print "Wait For Message ..."
while True:
    (Message, Address) = UDPSocket.recvfrom(BUFFER)
    print "Message : " + Message
    if Message == "exit":
        break
UDPSocket.close()
os._exit(0)
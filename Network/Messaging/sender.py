from socket import *

HOST = '169.254.243.180'
PORT = 80
Address = (HOST, PORT)
UDPSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    Message = raw_input("Enter Message : ")
    UDPSocket.sendto(Message, Address)
    if Message == "exit":
        break
UDPSocket.close()

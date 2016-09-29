from socket import *
try:
    from Crypto.Cipher import PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Hash import SHA
except ImportError:
    raise ImportError('You Should Run This Script Using Python 3 !!')
HOST = '192.168.1.101' #destiny IP address
PORT = 80 #destiny port number
Address = (HOST, PORT)
UDPSocket = socket(AF_INET, SOCK_DGRAM)
key = RSA.importKey(open('pubkey.der').read())
while True:
    Message = input("Enter Message : ")
    UDPSocket.sendto(Message, Address)
    if Message == "exit":
        break
UDPSocket.close()

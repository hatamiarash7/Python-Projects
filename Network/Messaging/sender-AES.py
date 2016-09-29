from socket import *
try:
    from Crypto.Cipher import AES
    from Crypto import Random
except ImportError:
    raise ImportError('You Should Run This Script Using Python 3 !!')

HOST = '192.168.1.101' #destiny IP address
PORT = 80 #destiny port number
Address = (HOST, PORT)
UDPSocket = socket(AF_INET, SOCK_DGRAM)
KEY = b'Sixteen byte key'
IV = Random.new().read(AES.block_size)
while True:
    Message = input("Enter Message : ")
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    cipher_text = IV + cipher.encrypt(b'Sixteen byte key')
    UDPSocket.sendto(cipher_text, Address)
    if Message == "exit":
        break
UDPSocket.close()

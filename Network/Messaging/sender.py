import socket

HOST = '192.168.1.112'
PORT = 4210
Address = (HOST, PORT)
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSocket.connect((HOST,PORT))
while True:
    Message = input("Enter Message : ")
    UDPSocket.send(Message.encode())
    if Message == "exit":
        break
UDPSocket.close()

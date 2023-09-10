from socket import *

serverPort = 1500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('201.213.57.185', serverPort))
print("El servidor está listo para recibir")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
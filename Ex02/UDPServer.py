from socket import *

serverPort = 12000 # Port number of your server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive!")

while True:
    print("-----------------------")
    receivedMessage,clientAddress = serverSocket.recvfrom(2048)
    clientIP, clientPort = clientAddress
    print(f"Connection from IP address: {clientIP} and port: {clientPort}")
    print("Received message: " + str(receivedMessage.decode()))
    modifiedMessage = receivedMessage.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
    print("Sent message: " + str(modifiedMessage.decode()))
    
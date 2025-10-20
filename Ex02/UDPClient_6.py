from socket import *

serverName = '163.143.11.43' # IP address of your server
serverPort = 12000  # Port number of your server
destAddress=(serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)

sequenceNumber = 1

while True:
    print("-----------------------")
    message = input("Input lowercase sentence:")

    messageWithSequenceNumber = f"{sequenceNumber}: {message}"

    clientSocket.sendto(messageWithSequenceNumber.encode(),destAddress)
    print(f"Sent message: {message} wiht sequence number {sequenceNumber}")
    receivedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Received message: " + str(receivedMessage.decode()))

    sequenceNumber += 1
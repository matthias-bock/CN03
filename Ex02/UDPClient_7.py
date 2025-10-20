from socket import *
from time import time
from datetime import datetime

serverName = '163.143.11.43' # IP address of your server
serverPort = 12000  # Port number of your server
destAddress=(serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)

sequenceNumber = 1

while True:
    print("-----------------------")
    message = input("Input lowercase sentence:")

    messageWithSequenceNumber = f"{sequenceNumber}: {message}"

    # Get timestamp when the message was sent
    sentAt = time()

    clientSocket.sendto(messageWithSequenceNumber.encode(),destAddress)
    print(f"Sent message: {message} wiht sequence number {sequenceNumber}")
    print(f"Message sent at {datetime.fromtimestamp(sentAt)}")
    receivedMessage, serverAddress = clientSocket.recvfrom(2048)

    # Get timestamp when the response was received
    receivedAt = time()

    print("Received message: " + str(receivedMessage.decode()))
    print(f"Received response at {datetime.fromtimestamp(receivedAt)}")

    # Compute the round trip time
    rtt = receivedAt - sentAt

    print("---")
    print(f"RTT: {rtt} seconds")
    print("---")

    sequenceNumber += 1

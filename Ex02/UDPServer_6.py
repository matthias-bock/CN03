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

    # Split message at ':' to extract sequence number
    messageParts = receivedMessage.decode().split(":")

    # Convert sequence number to integer
    sequenceNumber = int(messageParts[0])

    # In case the received message had multiple ':', recombine the remaining message
    clientMessage = ":".join(messageParts[1:])

    print("Received message: " + str(clientMessage))
    print(f"Sequence number: {sequenceNumber}")
    modifiedMessage = clientMessage.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("Sent message: " + str(modifiedMessage))
    
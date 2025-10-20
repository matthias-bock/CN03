from socket import *

serverPort = 12000 # Port number of your server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('0.0.0.0', serverPort))
print("The server is ready to receive!")

while True:
    print("-----------------------")
    receivedMessage,clientAddress = serverSocket.recvfrom(2048)
    clientIP, clientPort = clientAddress
    print(f"Connection from IP address: {clientIP} and port: {clientPort}")

    # Split message at first ':' to extract sequence number
    messageParts = receivedMessage.decode().split(":", maxsplit=1)

    # Convert sequence number to integer
    sequenceNumber = int(messageParts[0])

    # Extract the client message and remove additional " " characters at the start and end
    clientMessage = messageParts[1].strip(" ")

    print("Received message: " + str(clientMessage))
    print(f"Sequence number: {sequenceNumber}")
    modifiedMessage = clientMessage.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("Sent message: " + str(modifiedMessage))
    
import _thread
from socket import *
import time

def handleClient(connectionSocket):
    while True:
        message = connectionSocket.recv(1024).decode()

        # Do not process empty messages
        if len(message) == 0:
            continue

        # Remember when the message was received
        recvTime = time.time()

        # Split the message at ';'
        # The client message has the following format:
        # [Sentence];[Time when the client sent the message]
        messageParts = message.split(";")
        
        # Extract data from message parts
        sentence = messageParts[0]
        clientSentAt = float(messageParts[1])
        
        # Calculate time delay from client to server
        clientToServer = recvTime - clientSentAt

        capitalizedSentence = sentence.upper()

        # Build the message to the client
        returnMessage = f"{capitalizedSentence};{clientToServer};{time.time()}"

        connectionSocket.send(returnMessage.encode())
    connectionSocket.close()
    
serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print(f"The server is ready to receive on port {serverPort}")
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    
    clientIP, clientPort = clientAddress

    print(f"Received connection from IP {clientIP} on port {clientPort}")

    #Note: for question-2, replace this loop by the thread call
    _thread.start_new_thread(handleClient,(connectionSocket,))
    ############## 
    
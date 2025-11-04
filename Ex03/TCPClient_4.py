import _thread
from socket import *
import time

# Create a connect to Server 1
server1Name = '163.143.11.43' # IP address of your server
server1Port = 12000
destAddress1 = (server1Name,server1Port)
clientSocket1 = socket(AF_INET, SOCK_STREAM)
clientSocket1.connect(destAddress1)


# Create a connection to Server 2
#.........................................



def connectServer(clientSocket,sentence):

    # Send the time the message was sent at to the server
    message = f"{sentence};{time.time()}"
    clientSocket.send(message.encode())

    serverMessage = clientSocket.recv(1024).decode()

    # Remember when the response was received
    recvTime = time.time()

    # Split the message at ';'.
    # The server response has the following format:
    # [Modified sentence];[Delay client -> server];[Time when server sent the reply]
    serverMessageParts = serverMessage.split(";")

    # Extract information from the message parts
    clientToServer = float(serverMessageParts[1])

    # Calculate the delay from server to client by subtracting the receive time from the send time
    serverToClient = recvTime - float(serverMessageParts[2])

    print(f"Modified sentence: {serverMessageParts[0]}")
    print(f"Client -> Server:  {clientToServer}")
    print(f"Server -> Client:  {serverToClient}")
    
    # Estimate the RTT by adding the two one way trip delays
    print(f"Estimated RTT:     {clientToServer + serverToClient}")


while True:
    sentence = input("Input lowercase sentence:")

    connectServer(clientSocket1,sentence)
    
clientSocket1.close()
#close other sockets here

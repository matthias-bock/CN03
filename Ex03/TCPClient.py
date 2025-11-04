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
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())


while True:
    sentence = input("Input lowercase sentence:")
    connectServer(clientSocket1,sentence)
    
clientSocket1.close()
#close other sockets here

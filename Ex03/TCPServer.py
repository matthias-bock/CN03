import _thread
from socket import *

def handleClient(connectionSocket):
    while True:
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
    
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    
    clientIP, clientPort = clientAddress

    print(f"Received connection from IP {clientIP} on port {clientPort}")

    #Note: for question-2, replace this loop by the thread call
    while True:		
        sentence = connectionSocket.recv(1024) 
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
    connectionSocket.close()    
    ############## 
    
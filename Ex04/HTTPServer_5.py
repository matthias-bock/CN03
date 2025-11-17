from socket import * 
import sys 
from time import time
from uuid import uuid4

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1200
serverAddr = '163.143.11.43'

# Bind the socket to server address and server port, then listen
serverSocket.bind((serverAddr, serverPort))
serverSocket.listen(1)

def logRequest(clientIP, clientPort, fileSize, contentType, statusCode):
    
    clientID = uuid4().hex

    with open("server.log", "a") as f:
        f.write(f"User id: {clientID}\n")
        f.write(f"Timestamp: {time()}\n")
        f.write(f"Client IP: {clientIP}\n")
        f.write(f"Client Port: {clientPort}\n")
        f.write(f"Content type: {contentType}\n")
        f.write(f"Status code: {statusCode}\n")
        f.write(f"File size: {fileSize}\n")
        f.write("----------------\n")

while True:
    print('The server is ready to receive')
    # Set up a new connectio        logRequest(addr[0], addr[1], len(outputdata), "image/png", 200)n from the client
    connectionSocket, addr = serverSocket.accept()
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(99999999).decode() #should have .decode()
        # Extract the path o        logRequest(addr[0], addr[1], len(outputdata), "image/png", 200)f the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:],'rb')
        outputdata = f.read()     # Store the file in a temporary buffer
        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n".encode())  # should have .encode() 

        logRequest(addr[0], addr[1], len(outputdata), "image/png", 200)

        # Send the content of the requested file to the connection socket
        connectionSocket.send(outputdata)


        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()
    except IOError: # Using for Questions 2 and 3
        connectionSocket.send(f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
        message404 = f"<head> \
                                <title>404</title> \
                              </head> \
                              <body> \
                                <center> \
                                    <h1>404</h1> \
                                    <h3>The file {filename[1:]} was not found</h1> \
                                    <p>Client Port: {addr[1]}</p> \
                                    <p>Did you mean <a href='image.png'>image.png</a>?</p> \
                                </center> \
                              </body>"
        connectionSocket.send(message404.encode())
        connectionSocket.send("\r\n".encode())

        logRequest(addr[0], addr[1], len(message404), "text/html", 404)

        connectionSocket.close()
serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
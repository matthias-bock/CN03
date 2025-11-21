from socket import * 
import sys 
from uuid import uuid4
import base64

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1300
serverAddr = '163.143.11.43'

# Bind the socket to server address and server port, then listen
serverSocket.bind((serverAddr, serverPort))
serverSocket.listen(1)


while True:
    print('The server is ready to receive')
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    try:

        userID = uuid4().hex

        # Receives the request message from the client
        message = connectionSocket.recv(99999999).decode() #should have .decode()
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        print(filename[1:])
        f = open(filename[1:],'rb')
        outputdata = base64.b64encode(f.read())     # Store the file in a temporary buffer
        # Send the HTTP response header line to the connection socket
        connectionSocket.send(f'HTTP/1.1 200 OK\r\n\
Content-type: text/html\r\n\
My-Custom-ID: {userID}\r\n\r\n \
    <html><body>\
        <center>\
            <h1>User ID: {userID}</h1>\
            <img src="data:image/png;base64,{outputdata.decode()}">\
        </center>\
    </body></html>'.encode())  # should have .encode() 

        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close()
    except IOError: # Using for Questions 2 and 3
    #    connectionSocket.send("..........................................".encode())
    #    ...............................................................
        connectionSocket.close()
serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data

from socket import *
import time

starttime = time.time() # Use this line for to compute delay

serverName = 'www.nhk.or.jp' # Use this line for question 1

######DON'T CHANGE THIS PART!!!#######
serverPort = 1
destAddress = (serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
type_of_message = b'\x08'
code = b'\x00'
identifier = b'\x00\x01'
sequence_number = b'\x00\x01'

# Ones complement sum = 0x0800 + 0x0001 + 0x0001 = 0x0802
# Ones complement = 0xFFFF - 0x0802 = 0xF7FD

checksum = b'\xF7\xFD'

message = type_of_message + code + checksum + identifier + sequence_number

# send the request
clientSocket.sendto(message, destAddress)
# start to receive the reply. Note: this is just a part of
# the response. We will learn to receive a whole response later 
response = int.from_bytes(clientSocket.recv(2048), byteorder='big')
clientSocket.close()
# finish receiving the reply
######################################


#### Question 1
#print reply message here
print(f"{hex(response)}")
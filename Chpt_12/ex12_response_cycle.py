#You are to retrieve the following document using the HTTP protocol in a way that you can
#examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt

#Import the library
import socket

#Create socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect socket
mysock.connect(('data.pr4e.org', 80))

#Request documents
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#Receiving data
while True:
    data = mysock.recv(512)
    #End loop if end of data
    if len(data) < 1:
        break
    print(data.decode(),end='')

#Close the socket
mysock.close()
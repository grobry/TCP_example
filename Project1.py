# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET,SOCK_STREAM)

# Prepare a server socket on a particular port
serverPort = 6789

# Fill in code to set up the port
serverSocket.bind(("",serverPort))
serverSocket.listen()

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket,addr = serverSocket.accept()
    try:
        print("Connected")
        message = serverSocket.recv(1024)
        filename = message.split()[1]
        # Fill in security code
        f = open("HelloWorld.html", "r") # Fill in code to read data from the file
        # Send HTTP header line(s) into socket
        # Fill in code to send header(s)
        outputdata = f.readlines()
        serverSocket.sendall(outputdata.encode('utf-8'))
        # Send the content of the requested file to the client
        for i in range (0,len(outputdata)) :
            connectionSocket.send(outputdata[i].encode() )
            connectionSocket.send ("\r\n".encode())
            connectionSocket.close()
    except IOError:
        # Send response message for file not found
        print(f"File not found")
        # Close client socket
        serverSocket.close()
        sys.exit() # Terminate the program after sending the corresponding data
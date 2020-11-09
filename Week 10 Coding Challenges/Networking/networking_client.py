#Script: networking_client.py
#Author: Mahalakshmi Subramanian
#Anita Borg - Python Certification Course

#DESCRIPTION: A python script to define client and bind with server by establishing a socket connection.
#             A connection object is created to send encrypted messages with maximum size of 1024 bytes to the server

''' Sample data
Client sends: Jlkqv Mvqelk
Server sends back:Received: Jlkqv Mvqelk
Translation: monty python
'''

import socket
import time

# declare client host and port
host = 'localhost'
port = 4000

# creating socket object and then bind with server
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((host,port))

#print("Listening")
my_socket.listen(1)

#server accepts the socket and return connection object and address
connection, address = my_socket.accept()
#print("Connection from:", str(address))
#print("Connection object", connection)

#using the connection object send messages as bytes using 'b' or encode()
connection.send(b"Jlkqv Mvqelk")
time.sleep(0.1)
connection.send("QEXKH VLR XKFQXYLOD".encode())
time.sleep(0.1)
connection.send("f zlria dl clo pljb QXZLP".encode())

my_socket.close()
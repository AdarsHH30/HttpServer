import socket
import time

#Set the server host and port
SERVER_HOST="0.0.0.0"
SERVER_PORT=8080

#Create a socket object
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Allows the socket to reuse the address after the server is closed
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.setblocking(False)

#0 to 1023 are reserved ports for system use 
server_socket.bind((SERVER_HOST,SERVER_PORT))


#Listen for incoming connections
#5 is the maximum number of connections that can be queued
server_socket.listen(5)

print(f"Server is listening on port {SERVER_PORT}...")



while True:
    try:
        #Accept is the function that accepts incoming connections and returns a new socket object representing the connection and the address of the client
        client_socket,client_address = server_socket.accept()

        print(f"Connection from {client_address}")
        print(f"Client socket: {client_socket}")

    except :
        time.sleep(1)
        print("Error connecting to client") 
        continue
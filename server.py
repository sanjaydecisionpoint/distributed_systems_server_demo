# server.py
import socket
import sys

SERVER = 'localhost'
PORT = int(sys.argv[1])
INTERNAL_PORT = int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = (SERVER,PORT)
server_address_2 = (SERVER,INTERNAL_PORT)
sock.bind(server_address)
sock2.bind(server_address_2)

sock.listen(1)
sock2.listen(1)

msg = "Hello"

def msg_receiver():
    print("Starting Listening")
    while True:
        connection_1, client_address_1 = sock2.accept()
        try:
            print("Listening...")
            while True:
                global msg
                msg = connection_1.recv(1024).decode()
                print("Message received:: "+msg)
                break
        finally:
            connection_1.close()

def msg_sender():
    print("Starting Sending")
    while True:
        connection, client_address = sock.accept()
        try:
            
            print("Connected with ::", client_address)
            while True:
                global msg
                print("Message",msg)
                connection.send(bytes(msg,'utf-8'))
                print("Data sent::",msg)
                break
        finally:
            connection.close()

import threading

recv_thread = threading.Thread(target = msg_receiver,daemon=True)
sender_thread = threading.Thread(target = msg_sender,daemon=True)

recv_thread.start()
print("Recieve started")

sender_thread.start()
print("Sender started")

recv_thread.join()
sender_thread.join()

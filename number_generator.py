# number_generator.py
import socket
import random
import time
import sys

  
# connect it to server and port
# number on local computer.
def update(port,number):
    try:
        
        s = socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)
        print("Port::",port)
        s.connect(('localhost',port))

        s.send(str(number))
    finally:
        s.close()


while True:
    print("Executing..")
    time.sleep(5)
    number = random.randint(1,1000)
    update(int(sys.argv[1]),number)
    update(int(sys.argv[2]),number)




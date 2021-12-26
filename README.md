# CAP theorem Demo using simple messaging servers

## Purpose

To demo the CAP theorem by creating couple of instance of servers that can send and receive messages.
The servers can be primed to send same random number using number_generator script. It can be passed with receiving ports of the local servers and it will update them with the same random number every 5 seconds.
These servers can be then be telnetted on the sending ports where they emit the latest updated number they have.

The server file can be started by passing the ports for sending and receiving in the start command:
>python3 server.py 8000 8001

This will create an instance of the server that is listening on port 8000 and 8001. On 8001 it is receiving, so it will update its send message to be sent via 8000 with whatever it received on 8001.


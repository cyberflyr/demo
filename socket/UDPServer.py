#!/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive.")
while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    print(message, clientAdress)
    modifiedMessage = bytes.decode(message).upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAdress)

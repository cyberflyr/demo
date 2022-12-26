#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from socket import *

if __name__ == "__main__":

    serverName = "localhost"
    serverPort = 12000

    for i in range(10):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        sentence = f"hello gzz {i}\n"
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print(bytes.decode(modifiedSentence))
        time.sleep(0.5)
        clientSocket.close()

from socket import *


serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
for i in range(10):
    message = f"Input lowercase sentence: {i}"
    clientSocket.sendto(message.encode(), (serverName, serverPort))
for _ in range(10):
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    # print(modifiedMessage, serverAddress)
    print(bytes.decode(modifiedMessage), serverAddress)
clientSocket.close()

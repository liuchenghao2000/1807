from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

bindAddr = ('',41700)
udpSocket.bind(bindAddr)

while True:
    recvData = udpSocket.recvfrom(1024)
    print(msg )




udoSocket.close()

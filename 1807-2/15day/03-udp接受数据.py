from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

sendAddr = ('192.168.43.84',8080)

sendData = input('请输入要发送的数据')

udpSocket.sendto(sendData,sendAddr)

recvData = udpSocket.recvfrom(1024)

print(recvData)

udpSocket.close()

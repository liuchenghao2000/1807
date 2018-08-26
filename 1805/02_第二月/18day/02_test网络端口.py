#
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.sendto('今晚不吃饭'.encode('gb2312'),('192.168.43.28',8080))
#windows 网络接口
s.close()


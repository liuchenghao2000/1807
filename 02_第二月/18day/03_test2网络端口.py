#测试
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
while True:
	send_msg = input('msg')
	s.sendto((send_msg+'\n').encode('gb2312'),('192.168.43.28',8080))
s.close()
#测试
from socket import *
s = socket(AF_INET,SOCK_DGRAM)#创建一个udp的套接字
s.bind(('',8888))#绑定端口
#发送
s.sendto('今晚不吃'.encode('gb2312'),('192.168.43.28',8080))
while True:
	msg= s.recvfrom(1024)#数据接收
	#数据拆析
	print('信息:%s来自:%s'%(msg[0].decode('gb2312'),msg[1][0]))
#关闭进程
s.close()
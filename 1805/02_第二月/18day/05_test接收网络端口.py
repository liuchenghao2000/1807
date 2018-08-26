#测试
from socket import *
s = socket(AF_INET,SOCK_DGRAM)#创建一个udp的套接字
s.bind(('',8888))#绑定端口

while True:
	#发送
	sendmsg=input('msg')
	#数据编码
	s.sendto((sendmsg+'\n').encode('gb2312'),('192.168.43.28',8080))
	#接收
	msg= s.recvfrom(1024)
	#数据拆析
	print('信息:%s\n来自:%s'%(msg[0].decode('gb2312'),msg[1][0]))
#关闭进程
s.close()
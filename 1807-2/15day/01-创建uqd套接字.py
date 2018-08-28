from socket import *
#创建一个upd的套接字
s = socket(AF_INET,SOCK_DGRAM)
#对方IP 端口
s.sendto('我是老刘'.encode('gb2312'),('192.168.43.84',8080))

s.close()

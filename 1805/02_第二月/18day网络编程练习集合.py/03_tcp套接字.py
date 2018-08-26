#
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('192.168.43.28',6688))

content = input('请输入内容')

s.send(content.encode('gb2312'))
def recv():
	while True:
		global s
		global content
		msg = s.recv(1024)
		print(msg.decode('gb2312'))


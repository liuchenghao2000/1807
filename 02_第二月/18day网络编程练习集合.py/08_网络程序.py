#发送接受信息
from threading import Thread
from socket import *


def send():
	while True:
		content = input('请输入内容')
		s.sendto(content.encode('gb2312'),(ip,port))
def recv():
	while True:
		msg = s.recvfrom(1024)
		print('\n'+msg[0].decode('gb2312')+'  ')
		print(msg[1][0],end='\t')
		#print('请输入发送内容:')
def main(port=8080,ip='192.168.43.28'):
	global s
	global ip
	global port

	s = socket(AF_INET,SOCK_DGRAM)
	s.bind(('',8888))

	t = Thread(target = send)
	t1 = Thread(target = recv)

	t.start()
	t1.start()
	t.join()
	t1.join()

port = int(input('请输入对方端口'))
ip = input('请输入对方IP')
main()
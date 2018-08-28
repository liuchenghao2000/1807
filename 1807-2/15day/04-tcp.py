from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.43.97',2564))
s.listen(5)
s1.info = s.accept()
print('有新连接了')

print(s1.recv(1024).decode('gb2312'))
s1.send('哈哈'.encode('gb2312'))

s1.close()
s.close()
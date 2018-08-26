from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('',8880))
s.listen(5)
client,address= s.accept()
msg = client.recv(1024)
print(msg.decode('gb2312'))
client.send('哈哈'.encode('gb2312'))
client.close()

s.close()
#coding=utf-8
import socket
import select
#import Thread



#服务器配置信息
host = socket.gethostname()
print(host)

port = 5900

server_addr = (host,port)

#coding=utf-8
import socket
import select
#import Thread



#服务器配置信息
host = socket.gethostname()
print(host)

port = 5900

server_addr = (host,port)


inputs = []

fd_name = {}



def serverInit():
    ss = socket.socket()
    ss.bind(server_addr)
    se.listen(10)

    return ss

def newConnection(ss):
    client_conn,client_addr = ss.accept()
    try:
        client_conn.send("welcome to chatroom.pls set up your nick name!")
        

    except Exception as e:
        print(e)

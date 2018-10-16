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
        client_name = client_conn.recv(1024)
        inputs.append(client_conn)
        fd_name(client_conn) = client_name#将连接/连接明 加入键值对
        client_conn,send("current members in chatroom are: %s" % fd_name.values())

        #向所有连接发送成员信息
        for other in fd_name.keys():
            if other != client_conn and other != ss:
                other.send(fd_name[client_conn]+"joined the chatroom!")
                
    except Exception as e:
        print(e)

def closeConnection():
    pass


  


        

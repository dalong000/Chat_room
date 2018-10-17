#coding=utf-8

import socket
import select
import threading
import sys

host = ''
port = 9000

client_addr = (host,port)

#倾听其他成员谈话

def listening(cs):
    inputs = [cs]
    rlist,wlist,elist = select.select(inputs, [] , [])
    if cs in rlist:
        try:
            print(cs.recv(1024))
        except secket.error:
            print("socket is error")
            exit()

def speak(cs):
    while True:
        try:
            data = raw_input()
        except Exception as e:
            print("can't input")
            exit()


        try:
            cs.send(data)
        except Exception as e:
            exit()

def main():

    cs = socket.socket()
    cs.connect(client_addr)

    t = threading.Thread(target = listening,args = (cs,))
    t.start()

    t1 = threading.Thread(target = speak,args = (cs,))
    t1.start()

if __name__ == "__main__":
    main()


    
#





    
        

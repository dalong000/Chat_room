#coding=utf-8

import socket
import select
import threading
import sys

host = ''
port = 9000

client_addr = (host,port)

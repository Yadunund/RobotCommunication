# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:41:37 2019

@author: Yadunund Vijay

TCP/IP Client Software capable of receiving messages in a thread
"""

import numpy as np
import socket
import time 
import threading


received_string=''
send_string=''

server_ip='127.0.0.1'
server_port=65432


connected=False

def client_connect():
    global s, connected
    while True:
        try:
            if (connected==False):
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((server_ip,server_port))
                print('Connected to Server')
                time.sleep(0.5)
                connected=True
        except Exception as e:
            print("Error"+str(e))
            connected= False
            
def client_recv():
    global s, received_string, connected
    while True:
        try:
            if connected:
                received_string=s.recv(1024).decode()
                print('Received:'+received_string)
        except Exception as e:
            print("Error"+str(e))
            connected=False
            s.close()
            
#creating treads
            
            
thread_connect=threading.Thread(target=client_connect)
#thread_recv=threading.Thread(target=client_recv)

thread_connect.start()
#thread_recv.start()
                
    
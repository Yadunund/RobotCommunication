# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:50:51 2019

@author: Yadunund
"""

import threading
import socket 
import time, datetime

robot_IP = "127.0.0.1"
robot_port=65432
received_string=""

s= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

connected=False
conn=None
addr=None
s.bind((robot_IP,robot_port))

def server():
        global s, connected, conn,addr,robot_IP,robot_port
        while True:
            print("Watiing for Client to connect")
            s.listen()
            conn,addr= s.accept()
            print('Connected by', addr)
            connected= True
            while(connected):
                try:
                    received_string=conn.recv(1024).decode()
                    if(received_string==''):
                        connected=False
                        break
                    else:                    
                        print("Receievd:"+received_string)
                except:
                    connected=False
                    break;


t=threading.Thread(target=server)

t.start()
#time.sleep(3)

#try:
#    while True:
#        print(datetime.datetime.now())
#        time.sleep(0.1)
#finally:
#    print("done")
    #s.close()
    

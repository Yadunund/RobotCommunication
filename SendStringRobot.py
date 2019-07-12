# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:17:56 2018

@author: Yadunund

Function to send string passed as arguement to robot
"""
import socket
def send_robot(send_string_robot):
    robot_IP="192.168.125.1"
    robot_port=5515
    received_string_robot=""
 
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        try:
            s.connect((robot_IP,robot_port))
            s.sendall(send_string_robot.encode())
            print('Sent:{}'.format(send_string_robot))
            while True:
                received_string_robot=s.recv(1024)
                print("Received:",received_string_robot)                
        except:
            #logging.error("Cannot Connect to Robot Controller")
            print('Cannot Connect to Robot Controller')
        finally:
            s.close()

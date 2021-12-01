import socket
import sys
import pickle
import threading
import socketserver

import random
import string
import json
import os
import argparse
import time
from _thread import *

host = socket.gethostbyname('0.0.0.0')           # Get local machine name
port = 8888 # Arbitrary non-privileged port

def get_list():
    Info=[]
    f = open("G:/Demo/python/Info.txt","r",encoding='utf-8')
    
    line = f.readline()
    while line:
        txt_data = eval(line)
        Info.append(txt_data)
        line = f.readline()
    print(Info)

get_list()



try:

    server_connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                      # Create a socket object
    print ('Socket created')
except socket.error as msg :
    print ('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
                    # Reserve a port for your service.
try:
    server_connect.bind((host, port))                     # Bind to the port
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
    
print ('Socket bind complete')
      
while True:
    
    # Wait for connections
    msg = server_connect.recvfrom(1024)
    message= msg[0]
    addr = msg[1]
    if not message:
        break
    
    Info = json.loads(message)
    reply = "ok" +message.decode()
    reply = bytes(reply, 'utf-8')
    server_connect.sendto(reply,addr)
    #print ('Message[' + str(addr[0]) + ':' + str(addr[1]) + '] - ' + str(message.strip()))
    
    if time.sleep(5):
        print('start')
        print(Info)
        with open('G:\Demo\Python\Info.txt', 'w') as temp_file:
            for item in Info:
                temp_file.write("%s\n" % item)
                file = open('Info.txt', 'r')
                print(file.read())
    else:
        print('the fiel goes here')
        print(Info)
        with open('G:\Demo\python\Info.txt', 'w') as temp_file:
            for item in Info:
                temp_file.write("%s\n" % item)
                file = open('G:\Demo\python\Info.txt', 'r')
                print(file.read())
server_connect.close()
""""
while (1):
    bytesAddressPair  = UDPServerSocket .recvfrom(1024)
    #read and store Info.txt
    file =open('C:/Python/Info.txt','w')
    file.write(pickle.loads(bytesAddressPair ))
    file.close()
    data = bytesAddressPair [0]
    addr = bytesAddressPair [1] 
    if not data: 
        break
    print(data.decode()+'msg')
    #store all client infomation
    Info = ["name","IP","TCP","UDP",["file"]]
    #store the log and sessions
    session = ["function","RQ","name","IP","UDP","TCP","file"]

    if data.decode() == '1':
        func = ('Register')
    elif data.decode() == '2':
        func = ('De_Register')
    elif data.decode() == '3':
        func = ('Publish')    
    elif data.decode() == '4':
        func = ('Remove')
    elif data.decode() == '5':
        func = ('Retrieve_all')
    elif data.decode() == '6':
        func = ('Retrieve_infot')
    elif data.decode() == '7':
        func = ('Search')
    elif data.decode() == '8':
        func = ('Download')   
    elif data.decode() == '9':
        func = ('Update')  
    else:
        print("Error Input")


reply = func + ' function activated: ' + data.decode()
reply = bytes(reply, 'utf-8')

UDPServerSocket.sendto(reply , addr)
print('Got connection from ', addr[0], '(', addr[1], ')',data.strip())
print(addr) 
UDPServerSocket.close()
"""

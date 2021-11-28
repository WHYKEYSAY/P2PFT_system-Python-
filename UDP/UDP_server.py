import socket
import sys
import pickle
import threading
import random
import string
import json
import os
import argparse
import time

#import numpy as np

 



""""
#check name function
def check(name_list):
    l = len(name_list)
    for j in range(0, l):
        if Name == name_list[j][2]:
            print(0)
            print(Register_denied)
        else:
            print(1)
            print(Register_accepted)
            Register.append(user_Register)
    return name_list

#del de_reg name func
def delete(sub_li):
    l = len(sub_li)
    for j in range(0, l):
        if Name == sub_li[j][2]:
            del sub_li[j]
            print(De_Register)           
    return sub_li
#publish 
def publish(sub_li):
    l = len(sub_li)
    for j in range(0, l):
        if Name == sub_li[j][2]:
            del sub_li[j]
            print(Publish_accepted)
        else:
            print(Publish_denied)            
    return sub_li
#remove 
def remove(sub_li):
    l = len(sub_li)
    for j in range(0, l):
        if Name == sub_li[j][2]:
            del sub_li[j]
            print(Publish_accepted)
        else:
            print(Publish_denied)            
    return sub_li
"""
""""

"""



HOST = '0.0.0.0'             # Get local machine name
PORT = 8888 # Arbitrary non-privileged port

def get_list():
    Info=[]
    f = open("C:/Python/Info.txt","r",encoding='utf-8')
    
    line = f.readline()
    while line:
        txt_data = eval(line)
        Info.append(txt_data)
        line = f.readline()
    print(Info)

get_list()




try :
    UDPServerSocket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
    
try:
    UDPServerSocket .bind((HOST, PORT))
    print ('Socket bind complete')

except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
        
    
while (1):
    bytesAddressPair  = UDPServerSocket .recvfrom(1024)
    file =open('C:/Python/Save.txt','w')
    file.write(pickle.loads(bytesAddressPair ))
    file.close()
    
    data = bytesAddressPair [0]
    addr = bytesAddressPair [1] 
    if not data: 
        break

    print(data.decode()+'msg')

    Register = []

    #store all client infomation
    Info = ["name","IP","TCP","UDP"]
    #store all client files
    Library=["name","IP","TCP","file"]
    #store the log and sessions
    session = ["function","RQ","name","IP","UDP","TCP","file"]

    counter = 0
    if data.decode() == '1':
        func = ('Register')
        counter = 0
        #keep = 0
        #change iteration limit; move to client.py
        #while keep != ('N' or "No" or "no"):
        """"
        while counter<3:            
            RQ_NO = '1' + str(counter)
            Name = input('Name: ')
            
            IP = input('IP Address: ')
            UDP_NO = input('UDP socket Number: ')
            TCP_NO = input('TCP socket Number: ')
            user_Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
            Register_accepted = ['REGISTER',RQ_NO]
            Register_denied = ['REGISTER_DENIED', RQ_NO, 'Name do not exist!']
            check(Register)
            print(user_Register)
            print(Register_accepted)
            print(Register_denied)
            counter += 1
            #keep = input("Continue? (Y/N)")
            
        print(Register)
        """
        #nest lists
    elif data.decode() == '2':
        func = ('De_Register')
        counter = 0    
        #same here   
        while input != ('EXIT'):
            
            RQ_NO = '2' + str(counter)
            Name = input('Name: ')    
            
            De_Register = ['DE_REGISTER', RQ_NO, Name]
            delete(Register)
            
            counter +=1
        

    elif data.decode() == '3':
        func = ('Publish')
        while input != ('EXIT'):

            #user input only 
            Name = input('Name: ')   
            List_of_files = input('List of files: ')
            Library = [Name,List_of_files]

            #server generate
            RQ_NO = '3' + str(counter)   
            Publish = ['PUBLISH', RQ_NO, Name, List_of_files]
            Publish_accepted = ['PUBLISH', RQ_NO]
            Publish_denied = ['PUBLISH_DENIED', RQ_NO, 'Name do not exist!']
            
            publish(Register) 
            counter +=1            

    elif data.decode() == '4':
        func = ('Remove')
        while input != ('EXIT'):
            RQ_NO = '4' + str(counter)
            Name = input('Name: ')   
            List_of_files_remove = input('List of files to remove: ')   
            Remove = ['REMOVE',RQ_NO,Name, List_of_files_remove]
            Remove_accepted = ['REMOVE',RQ_NO]
            Remove_denied = ['REMOVE',RQ_NO, 'Name do not exist!']
            remove(Register) 
            counter +=1       

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
        counter = 0
        #keep = 0
        #change iteration limit; move to client.py
        #while keep != ('N' or "No" or "no"):
        while counter<3:            
            RQ_NO = '1' + str(counter)
            Name = input('Name: ')
            
            IP = input('IP Address: ')
            UDP_NO = input('UDP socket Number: ')
            TCP_NO = input('TCP socket Number: ')
            user_Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
            Register_accepted = ['REGISTER',RQ_NO]
            Register_denied = ['REGISTER_DENIED', RQ_NO, 'Name do not exist!']
            check(Register)
            print(user_Register)
            print(Register_accepted)
            print(Register_denied)
            counter += 1
            #keep = input("Continue? (Y/N)")
            
        print(Register)
    else:
        print("Error Input")

reply = func + ' function activated: ' + data.decode()
reply = bytes(reply, 'utf-8')

s.sendto(reply , addr)
print('Got connection from ', addr[0], '(', addr[1], ')',data.strip())
print(addr) 
s.close()
"""
def TCP_session():
    s = socket.socket()                      # Create a socket object
    host = socket.gethostname()              # Get local machine name

    port = 12345                             # Reserve a port for your service.
    s = socket.socket()
    s.bind((host, port))                     # Bind to the port

    s.listen(5)                              # Now wait for client connection.

    def processMessages(conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                if not data: 
                    conn.close()
                print(data.decode("utf-8"))
                conn.sendall(bytes('Thank you for connecting', 'utf-8'))
            except:
                conn.close()
                print("Connection closed by", addr)
                # Quit the thread.
                sys.exit()


    while True:
        # Wait for connections
        conn, addr = s.accept()
        print('Got connection from ', addr[0], '(', addr[1], ')')
        # Listen for messages on this connection
        listener = threading.Thread(target=processMessages, args=(conn, addr))
        listener.start()

UDP_session()
msg_client = UDP_session.msg.recv(1024)

if msg_client == '1' or '2' or '3' or '4' or '7' or '9':
    UDP_session()
elif msg_client == '5' or '6' or '8':
    TCP_session()
    """
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

file = open('Y:/Save.txt','w')
file.write(str(data))
file.close()        
"""
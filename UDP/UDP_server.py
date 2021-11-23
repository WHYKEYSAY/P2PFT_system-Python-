import socket
import sys
import threading
from functions import * 

 
HOST = '0.0.0.0'             # Get local machine name
PORT = 8888 # Arbitrary non-privileged port



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

try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
try:
    s.bind((HOST, PORT))
    print ('Socket bind complete')

except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
 
while (1):
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1] 
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
        func = ('Research')
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

 
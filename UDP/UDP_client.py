import socket
import threading
import random
import string
import json
import os
import argparse
import time
import sys


client_host = '0.0.0.0'
client_port =  8889

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
s.bind((client_host,client_port))



"""
def TCP_session():
    host = socket.gethostname()              # Get local machine name
    port = 12345                            # Reserve a port for your service.
    conn = socket.socket()                   # Create a socket object

    conn.connect((host, port))

    conn.sendall(b'Connected. Wait for data...') 

    while 1:
        intosend = input("Your options:"+'\n'+"[1] Register"+'\t\t'+ "[2] De-Register"+'\t\t'+"[3] Publish"+'\n'+"[4] Remove"+'\t\t'+ "[5] Retrieve-all"+'\t'+"[6] Retrieve-infot"+'\n'+"[7] Research"+'\t\t'+ "[8] Download"+'\t\t'+"[9] Update"+'\n')
        conn.sendall(intosend.encode('utf-8'))
        print(intosend+'1')
        #data received back from sever
        data = conn.recv(1024)
        #print("Data: ", data.decode('utf-8'))
    conn.close()                                   # Close the socket when done
"""

   # print(data.decode("utf-8"))
#def function(msg):
#store all client infomation
Info = [["name","IP","TCP","UDP"],["name2","IP2","TCP2","UDP2"],["name3","IP3","TCP3","UDP3"]]
#Info =[]
#store all client files
Library=[["name","IP","TCP","file"],["name2","IP2","TCP2","file2"],["name3","IP3","TCP3","file3"]]
#Library = ["2"]
#store the log and sessions
Session = [["function","RQ","name","IP","UDP","TCP","file"],["function2","RQ2","name2","IP2","UDP2","TCP2",["file2","file22","fiel2"]],["function3","RQ3","name3","IP3","UDP3","TCP3",["file3","fiel23"]]]
#Session = ["3"]


while True :
    msg = input("Your options:"+'\n'+"[1] Register"+'\t\t'+ "[2] De-Register"+'\t\t'+"[3] Publish"+'\n'+"[4] Remove"+'\t\t'+ "[5] Retrieve-all"+'\t'+"[6] Retrieve-infot"+'\n'+"[7] Research"+'\t\t'+ "[8] Download"+'\t\t'+"[9] Update"+'\n')

    counter = 0
    if msg == "1":           
        while True:
            RQ_NO = '1' + str(counter)
            Name = input('Name to register: ') 
            IP = input('IP Address: ')
            UDP_NO = input('UDP socket Number: ')
            TCP_NO = input('TCP socket Number: ')
            user_Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
            Register_accepted = ['REGISTER',RQ_NO]
            Register_denied = ['REGISTER_DENIED', RQ_NO, 'Name do not exist!']
            Info_temp = [Name,IP,UDP_NO,TCP_NO]
            Session_temp = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
            l = len(Info)
            for i in range(0,l):
                if Name == Info[i][0]:
                    print(Register_denied)
                else:
                    print(Register_accepted)
                    Info.append(Info_temp)
                    Session.append(Session_temp)
                    break
            print(Info)
            print(Session)
            counter+=1         
            break

    elif msg == '2':
        
        while True:
            RQ_NO = '2' + str(counter)
            Name = input('Name to deregister: ')          
            De_Register = ['DE_REGISTER', RQ_NO, Name]
            #Session_temp = ['DE_REGISTER', RQ_NO, Name,IP,UDP_NO,TCP_NO]
            for i in range(0,len(Info)):
                if Name == Info[i][0]:
                    del Info[i]
                    print(De_Register)
                # print(Session_temp)
        
            print(Info)
            print(Session)      
            counter +=1      

            break

    elif msg == '3':  

        while True:
            RQ_NO = '3' + str(counter)   
            Name = input('Name to publish: ')   
            List_of_files = input('List of files to publish: ')
            Library = [Name,List_of_files]
            Publish = ['PUBLISH', RQ_NO, Name, List_of_files]
            Publish_accepted = ['PUBLISH', RQ_NO]
            Publish_denied = ['PUBLISH_DENIED', RQ_NO, 'Name do not exist!']
            i = 0
            for sublist in Library:
                for i in range(0,len(Library)):

                    # name verified, store the lists
                    if Name == Library[i-1][0]:
                        Library[i-1][1].append(List_of_files)
                        print(Publish_accepted)
                    else:
                        print(Publish_denied)
                        break
            print(Library)
            counter += 1             
            break

    elif msg =='4':
        while True:
            RQ_NO = '4' + str(counter)
            Name = input('Name to remove: ')   
            List_of_files_remove = input('List of files to remove: ')   
            Remove = ['REMOVE',RQ_NO,Name, List_of_files_remove]
            Remove_accepted = ['REMOVE',RQ_NO]
            Remove_denied = ['REMOVE',RQ_NO, 'Name do not exist!']
            for sublist in Library:
                for i in range(0,len(sublist)):
                    #name exit, remove
                    if List_of_files_remove == Library[i-1][0]:
                        for j in range(0,len(Library[i-1][1])):
                            #file exit, remove
                            if List_of_files_remove == Library[i-1][1][j-1]:
                                del Library[i-1][1][j-1]
                                print("Remove_accepted")
                            else:
                                print("file doesnt exit!") 
                    else:
                        print("Remove_denied")   

            print(Library)
            counter += 1
            break

    elif msg == '5':
        #TO-DO switch to TCP seesion
    
        while True:
            RQ_NO = '5' + str(counter)
            Name = input('Name to retrieve-all: ')   
            for sublist in Library:
                for counter in range(0,len(Library)):
                    #name exit, research
                    print(counter, "->", Library[counter])
                    print(len(sublist))
                    if Name == Library[counter][0]:
                        print("matched!")
                        print("\n Retrived-all ", RQ_NO,"\n")
                        for sub_list in Library:
                            if sub_list[:3]:
                                print("\n",sub_list[:3],"\n The lists of files are shown as following: ")
                                for x in sub_list[3:]:
                                    print(x)
                                print

            print(Library)
            counter +=1
            break

    elif msg =='6':

        while True:
            RQ_NO = '6' + str(counter)
            Name = input('Name to retrieve-info: ')

            for sublist in Library:
                for counter in range(0,len(sublist)-1):
                    #name exit, research
                    print(counter, "->", Library[counter])
                    print(len(sublist))
                    if Name == Library[counter][0]:
                        print("matched!") 
                    if input("name to display") ==  Library[counter][0]:
                        print("\n Retrived-info ", RQ_NO,"\n")
                        if Library[counter][:3]:
                            print("\n",Library[counter][:3],"\n The lists of files are shown as following: ")
                            for x in Library[counter][3:]:
                                print(x)
                            print    
            
            print(Library)
            counter +=1
            break

    elif msg == '7':

        while True:
            RQ_NO = '7' + str(counter)
            Name = input('Name to research: ')
            research_file = input("book: ")  
            for sublist in Library:
                for counter in range(0,len(sublist)-1):
        #           name exit, research
                    print(counter, "->", Library[counter])
                    print(len(sublist))
                    if Name == Library[counter][0]:
                        print("matched!")
                        found = False
                        for sub_list in Library:
                            for i in range(0,len(sub_list)-1):
                                for j in range(0,len(Library[i][-1])):
                                #file exit, display name
                                    if research_file == Library[i][-1][j]:                           
                                        print("The list of files ","<<",research_file,">>"," is from: \n",Library[i][:3])
                                        found = True
                                        break
                            else:
                                print("file doesnt exit!")
                                break 
                    else:
                        print("research_denied")             
            print(Library)
            counter +=1
            break
        

    elif msg =='8':

        #TCP_session()
        while True:
            RQ_NO = '8' + str(counter)
            Name = input('Name to download: ')  




            print(Library)
            counter +=1
            break

    elif msg =='9':

        while True:
            RQ_NO = '9' + str(counter)
            Name = input('Name to update: ')
            IP = input('IP Address: ')
            UDP_NO = input('UDP socket Number: ')
            TCP_NO = input('TCP socket Number: ')
            user_Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
            Update_accepted = ['UPDATE',RQ_NO]
            Update_denied = ['UPDATE_DENIED', RQ_NO, 'Name do not exist!']
            Info_temp = [Name,IP,UDP_NO,TCP_NO]
            Session_temp = ['UPDATE',RQ_NO,Name,IP,UDP_NO,TCP_NO]
            l = len(Info)            
            for sublist in Info:
                for i in range(0,len(sublist)):
                    if Name != Info[i][0]:
                        print(Update_denied)
                        break
                    else:
                        print("match!")
                        if IP != Info[i][1]:
                            Info[i][1] = IP
                        if UDP_NO != Info[i][2]:
                            Info[i][2] = UDP_NO
                        if TCP_NO != Info[i][3]:
                            Info[i][3] = TCP_NO
                        
                        print(Info_temp)

                        
                    
                    print("successful!")
                else:
                    print("name doesnt exist!")
            print(Info) 

            print(Library)
            counter +=1
            break    

    else:
        print("please  input valid number!")
        time.sleep(3)
        break


print(Info,Session,Library)





try:
        
        s.sendto(msg.encode(), (client_host, client_port))
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
    
        print ('Server reply : ' + str(reply))
        
    
except socket.error as msg:
    print ('Error')
time.sleep(10)

    
while True:    
    token = input()
    if token == "y" or "Y" or "YES" or "yes" or "Yes" :   
        function()
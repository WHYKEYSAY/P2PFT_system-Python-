import socket
import threading
import random
import string
import json
import os
import argparse
import time
import sys
import pickle

client_host = '0.0.0.0'
client_port =  8889
#store all client files
Info=[["name","IP","UDP","TCP",["file","book"]],["name2","IP2","UDP2","TCP2",["book","file2"]],["name3","IP3","UDP3","TCP3",["file3"]]]
#store the log and sessions
Session = [["function","RQ","name","IP","UDP","TCP",["file"]],["function2","RQ2","name2","IP2","UDP2","TCP2",["file2","file22","fiel2"]],["function3","RQ3","name3","IP3","UDP3","TCP3",["file3","fiel23"]]]
try:
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
UDPClientSocket.bind((client_host,client_port))
def send_data():
    try:
        #Session = pickle.dump(Save)
        UDPClientSocket.sendto(Session, (client_host, client_port))
        msgFromServer  = UDPClientSocket.recvfrom(1024)
        reply = msgFromServer [0]
        addr = msgFromServer [1]
            
        print ('Server reply : ' + str(reply))
        print('ip is: ' + str(addr))
        
    except socket.error as Save:
        print ('Error')


counter = 0
while True :
    try:
        msg = input("Your options:"+'\n'+"[1] Register"+'\t\t'+ "[2] De-Register"+'\t\t'+"[3] Publish"+'\n'+"[4] Remove"+'\t\t'+ "[5] Retrieve-all"+'\t'+"[6] Retrieve-infot"+'\n'+"[7] Research"+'\t\t'+ "[8] Download"+'\t\t'+"[9] Update"+'\n')
        
        counter+=1
        if msg == "1":           
            while True:
                RQ_NO = '1_' + str(counter)
                Name = input('Name to register: ') 
                IP = input('IP Address: ')
                UDP_NO = input('UDP socket Number: ')
                TCP_NO = input('TCP socket Number: ')
                user_Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
                Register_accepted = ['REGISTER',RQ_NO]
                Register_denied = ['REGISTER_DENIED', RQ_NO, 'Name already exists!']
                Info_temp = [Name,IP,UDP_NO,TCP_NO,["File name: "]]
                Session_temp = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
                i = 0
                l = len(Info)
                for i in range(0,l):
                    if Name != Info[i][0]:
                        print(Register_accepted)
                        Info.append(Info_temp)
                        Session.append(Session_temp)
                        break
                    elif Name == Info[i][0]:
                        print(Register_denied)
                        break       
                break

        elif msg == '2':        
            while True:
                RQ_NO = '2_' + str(counter)
                Name = input('Name to deregister: ')          
                De_Register = ['DE_REGISTER', RQ_NO, Name]
                #Session_temp = ['DE_REGISTER', RQ_NO, Name,IP,UDP_NO,TCP_NO]
                i =0
                for i in range(0,len(Info)):
                    if Name == Info[i][0]:
                        del Info[i]
                        break      
                print(De_Register)
                break
        elif msg == '3':  
            while True:
                RQ_NO = '3_' + str(counter)   
                Name = input('Name to publish: ')   
                List_of_files = input('List of files to publish: ')
                Publish = ['PUBLISH', RQ_NO, Name, List_of_files]
                Publish_accepted = ['PUBLISH', RQ_NO]
                Publish_denied = ['PUBLISH_DENIED', RQ_NO, 'Name: <{}> do not exist!'.format(Name)]
                #Info_temp = [Name,IP,UDP_NO,TCP_NO]
                #Session_temp = ['PUBLISH',RQ_NO,Name,IP,UDP_NO,TCP_NO]

                for i in range(0,len(Info)):
                    # name verified, store the lists
                    if Name == Info[i][0]:
                        Info[i][-1].append(List_of_files)
                        print(Publish_accepted)
                        break
                        #Session.append(Session_temp)               
                if i == len(Info)-1:
                    print(Publish_denied)
                #send_data(Info)    
                print(Info)           
                break

        elif msg =='4':
            while True:
                RQ_NO = '4_' + str(counter)
                Name = input('Name to remove: ')   
                List_of_files_remove = input('List of files to remove: ')   
                Remove = ['REMOVE',RQ_NO,Name, List_of_files_remove]
                Remove_accepted = ['REMOVE',RQ_NO]
                Remove_name_denied = ['REMOVE',RQ_NO, 'Name: <{}> do not exist!'.format(Name)]
                Remove_file_denied = ['REMOVE',RQ_NO, 'Fiel Name: <{}> do not exist!'.format(List_of_files_remove)]
                i = 0
                for i in range(0,len(Info)):
                    #name exit, remove
                    if Name == Info[i][0]:
                        for j in range(0,len(Info[i][-1])):
                            #file exit, remove
                            if List_of_files_remove == Info[i][-1][j]:
                                del Info[i][-1][j]
                                print(Remove_accepted)
                                break
                        if j == len(Info)-1:
                            print(Remove_file_denied)
                        break 
                if i == len(Info)-1:
                    print(Remove_name_denied)   
                print(Info)
                break

        elif msg == '5':
            while True:
                RQ_NO = '5_' + str(counter)
                Name = input('Name to retrieve-all: ')
                Retrieve_all = ["RETRIEVE_ALL",RQ_NO]   
                
                for i in range(0,len(Info)):
                    #name exit, research
                    j =0
                    if Name == Info[i][0]:
                        print(Retrieve_all)
                        for sub_list in Info:                            
                            if sub_list[:4]:
                                print("\n",sub_list[:4],"\n The lists of {}'s files are shown as following: ".format(Info[j][0]))
                                j+=1
                                for x in sub_list[4:]:
                                    print(x)                        
                        print(i)
                        break   
                else:
                    print("Please input the Registered Name!")
                break
                

        elif msg =='6':
            while True:
                RQ_NO = '6_' + str(counter)
                Name = input('Name to retrieve-info: ')
                Retrieve_info_accepted = ["RETRIEVE_INFOT",RQ_NO]
                Retrieve_info_denied = ["RETRIEVE_INFOT",RQ_NO, "The Name: {} does not exist!".format(Name)]
                i = 0
                for i in range(0,len(Info)):
                    #name exit, research
                    if Name == Info[i][0]:
                        print("matched")
                        Name_to_display = input("name to display: ")
                        for j in range(0,len(Info)):
                            if  Name_to_display==  Info[j][0]:
                                print(Retrieve_info_accepted) 
                                print(Info[j][:4],"\n The lists of files are shown as following: ")
                                for x in Info[j][4:]:
                                    print(x)
                        break      
                else:
                    print(Retrieve_info_denied)
                    print("Please provide valid name!")
                break

        elif msg == '7':
            while True:
                RQ_NO = '7_' + str(counter)
                Name = input('Name to research: ')
                research_file = input("book: ")  
                
                for i in range(0,len(Info)):
                    #name exit, research
                    if Name == Info[i][0]:
                        print("matched!")
                        for sub_list in Info:
                            for n in range(0,len(sub_list)):
                                for j in range(0,len(Info[n][-1])):
                                #file exit, display name
                                    if research_file == Info[n][-1][j]:                           
                                        print("The list of files ","<<",research_file,">>"," is from: \n",Info[n][:4])
                                        found = True            
                            else:
                                print("file doesnt exit!")            
                else:
                    print("research_denied") 
                    break            

        elif msg =='8':
            #TCP_session()
            while True:
                RQ_NO = '8_' + str(counter)
                peer_ip = input('[CLIENT] What is IP of peer?: ')
                port_tcp = int(input('[CLIENT] What is port of peer?: '))

                target_file = input('[CLIENT] What file would you like to download from the peer?: ')
    




                print(Info)
                break

        elif msg =='9':
            while True:
                RQ_NO = '9_' + str(counter)
                Name = input('Name to update: ')
                IP = input('IP Address: ')
                UDP_NO = input('UDP socket Number: ')
                TCP_NO = input('TCP socket Number: ')
                user_Register = ['REGISTER',RQ_NO,Name,IP,UDP_NO,TCP_NO]
                Update_accepted = ['UPDATE',RQ_NO]
                Update_denied = ['UPDATE_DENIED', RQ_NO, 'Name: <{}> do not exist!'.format(Name)]
                Info_temp = [Name,IP,UDP_NO,TCP_NO]
                Session_temp = ['UPDATE',RQ_NO,Name,IP,UDP_NO,TCP_NO]
                l = len(Info)            
                for i in range(0,len(Info)):
                    if Name == Info[i][0]:                        
                        print("match!")

                        if IP != Info[i][1]:
                            Info[i][1] = IP
                        if UDP_NO != Info[i][2]:
                            Info[i][2] = UDP_NO
                        if TCP_NO != Info[i][3]:
                            Info[i][3] = TCP_NO
                        print(Info_temp)
                        break
                else:
                        print(Update_denied)
                break        
    except Exception as msg:
        print("please input valid number!",msg)
        
        







    

import socket
import sys
import threading
import UDP_server
from UDP_server import * 



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

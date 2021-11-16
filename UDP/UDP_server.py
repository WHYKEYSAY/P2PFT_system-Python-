import socket
import sys
import threading

 
HOST = '0.0.0.0'             # Get local machine name
PORT = 8888 # Arbitrary non-privileged port
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket created')
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
    print ('Socket bind complete')
 
while (1):
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1] 
    if not data: 
        break

    print(data.decode()+'msg')

    if data.decode() == '1':
        func = ('Register')
        #nest lists
    elif data.decode() == '2':
        func = ('De-Register')
    elif data.decode() == '3':
        func = ('Publish')
    elif data.decode() == '4':
        func = ('Remove')
    elif data.decode() == '5':
        func = ('Retrieve-all')
    elif data.decode() == '6':
        func = ('Retrieve-infot')
    elif data.decode() == '7':
        func = ('Research')
    elif data.decode() == '8':
        func = ('Download')   
    elif data.decode() == '9':
        func = ('Update')  
    else:
        print("Error Input")

    reply = func + ' function activated: ' + data.decode()
    reply = bytes(reply, 'utf-8')
    
    s.sendto(reply , addr)
    print('Got connection from ', addr[0], '(', addr[1], ')',data.strip())
    print(addr) 
s.close()

 
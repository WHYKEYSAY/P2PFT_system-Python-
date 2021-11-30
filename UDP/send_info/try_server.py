from pickle import loads
import socket
import threading
import sys
import json


host = '0.0.0.0'             # Get local machine name
port = 8888      
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

                        # Now wait for client connection.
"""
def processMessages(message, addr):
    message = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                      # Create a socket object

    while True:
        try:
            d = message.recvfrom(1024)
            data = d[0]
            addr = d[1]

            if not d: 
                break
            reply = "okk" + data
            #print(d.decode("utf-8"))
            message.sendto(bytes('Thank you for connecting', 'utf-8'),reply,addr)
        except:
            message.close()
            print("Connection closed by", addr)
            # Quit the thread.
            sys.exit()
"""

while True:
    
    # Wait for connections
    msg = server_connect.recvfrom(1024)
    print(msg)
    message= msg[0]
    addr = msg[1]
    if not message:
        break
    
    Info = json.loads(message)
    reply = "ok" +message.decode()
    reply = bytes(reply, 'utf-8')
    server_connect.sendto(reply,addr)
    print ('Message[' + str(addr[0]) + ':' + str(addr[1]) + '] - ' + str(message.strip()))
    print(Info)
    #Info =str(message)[2:len(message)+2]
    #print(Info)
    print(Info[0],Info[-1],Info[0][0])
    #print(type(*Info))
server_connect.close()
"""
    print(message)
    print(type(message))
    print('Got connection from ', addr[0], '(', addr[1], ')',server_connect)
    # Listen for messages on this connection
    listener = threading.Thread(target=processMessages, args=(message, addr))
    listener.start()
"""
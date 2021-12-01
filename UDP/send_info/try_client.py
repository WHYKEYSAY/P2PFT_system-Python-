import socket                            # Import socket module
import sys
import json

client_host = '0.0.0.0'             # Get local machine name
client_port = 8889                            # Reserve a port for your service.
                   # Create a socket object
try:
    server_connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
server_connect.bind((client_host,client_port))
host = 'localhost'
port = 8888
aaa =[["name","IP","UDP","TCP",["file","book"]],["name2","IP2","UDP2","TCP2",["book","file2"]],["name3","IP3","UDP3","TCP3",["file3"]]]

def send(list):

    while 1:

        msg = input("message to send:")
        if msg == '1':
            list.append(msg)
            print(list)
            print(type(list))

        else:
            try:

                Info = json.dumps(list)
                server_connect.sendto(bytearray(Info.encode()),(host,port))
                #data received back from sever
                data = server_connect.recvfrom(1024)

                print("Data: ", data)
                list_back = data[0]
                print(list_back)
                

            except socket.error as msg:
                print('Error')
    server_connect.close()                                   # Close the socket when done
send(aaa)

#print(data.decode("utf-8"))

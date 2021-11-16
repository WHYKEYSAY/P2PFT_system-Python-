import socket   #for sockets
import sys  #for exit
client_host = '0.0.0.0'
client_port =  8889

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
s.bind((client_host,client_port))
host = 'localhost'
port = 8888
 
while(1) :
    msg = input('Enter message to send : ')
    try:
         s.sendto(msg.encode(), (host, port))
         d = s.recvfrom(1024)
         reply = d[0]
         addr = d[1]
         
         print ('Server reply : ' + str(reply))
     
    except socket.error as msg:
        print ('Error')

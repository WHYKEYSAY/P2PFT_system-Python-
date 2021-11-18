import socket   #for sockets
import sys  #for exit
import time
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
    msg = input("Your options:"+'\n'+"[1] Register"+'\t\t'+ "[2] De-Register"+'\t\t'+"[3] Publish"+'\n'+"[4] Remove"+'\t\t'+ "[5] Retrieve-all"+'\t'+"[6] Retrieve-infot"+'\n'+"[7] Research"+'\t\t'+ "[8] Download"+'\t\t'+"[9] Update"+'\n')
    try:
         s.sendto(msg.encode(), (host, port))
         d = s.recvfrom(1024)
         reply = d[0]
         addr = d[1]
     
         print ('Server reply : ' + str(reply))
         
     
    except socket.error as msg:
        print ('Error')
    time.sleep(10)

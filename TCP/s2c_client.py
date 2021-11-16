import socket                            # Import socket module

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


print(data.decode("utf-8"))
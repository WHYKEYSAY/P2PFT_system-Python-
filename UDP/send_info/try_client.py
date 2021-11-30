import socket                            # Import socket module
import sys
def main():
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

#def function(server_connect,host,port):
    while 1:

        msg = input("message to send:")
        try:

            server_connect.sendto(msg.encode('utf-8'),(host,port))
            #data received back from sever
            data = server_connect.recvfrom(1024)
            print("Data: ", data)
        except socket.error as msg:
            print('Error')
    server_connect.close()                                   # Close the socket when done


    print(data.decode("utf-8"))
if __name__ == '__main__':
    main()
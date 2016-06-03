
import socket               # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '127.0.0.1'
port = 5001            # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
print("waiting for connection...")
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    print("Receiving...")
    with open('torecv.jpg','wb')as f: # Open file new file to write received data
        l = c.recv(1024)
        while (l):
            print("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print("Done Receiving")
    # c.send('Thank you for connecting')
        c.close()                # Close the connection

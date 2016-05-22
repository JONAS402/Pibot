#!/usr/bin/python
# working
# V1.0
# laptop version
import socket
import time


def Main():
    host = "127.0.0.1"
    port = 5001
    mySocket = socket.socket()
    mySocket.bind((host, port))
    mySocket.listen(1)
    print('waiting for connection...')
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("from connected  user: " + str(data))
        data = str(data).upper()
        print("Recieved from User: " + str(data))
        message = input("please enter message: ")
        conn.send(message.encode())
        print("message '{0}' sent to client".format(message))

    conn.close()


if __name__ == '__main__':
    Main()

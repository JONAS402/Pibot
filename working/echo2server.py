#!/usr/bin/python
# working
# V1.0
# LOCATED ON LAPTEOP
import socket
import time


def main():
    host = "127.0.0.1"
    port = 5001
    mySocket = socket.socket()
    mySocket.bind((host, port))
    mySocket.listen(1)
    print('waiting for connection...')
    conn, addr = mySocket.accept()
    address = str(addr)
    print("Connection from client: {0}".format(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        recieved = str(data)
        print("from connected  client: {0} Message: {1}".format(address, recieved))
        message = input("please enter message: ")
        conn.send(message.encode())
        print("message '{0}' sent to client".format(message))

    conn.close()


if __name__ == '__main__':
    main()

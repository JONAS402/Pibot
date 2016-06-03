#!/usr/bin/python
# working
# V1.0
# TODO
# login using hashlib sha224
# LOCATED ON LAPTOP
import socket
import hashlib
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
    username = input('enter username: ')
    conn.send(username.encode())
    reply = conn.recv(1024).decode()
    print(reply)
    if reply == 'Incorrect Username!':
        conn.close()
        exit()
    password1 = input('enter password 1: ')
    password12 = password1.encode('utf-8')
    pass1hash = hashlib.sha224(password12)
    pass1hash1 = str(pass1hash.hexdigest())
    conn.send(pass1hash1.encode())

    password2 = input('enter password 2: ')
    pass2_hash = hashlib.sha224(password2.encode('utf-8'))
    # pass2_hash1 = str(pass2_hash.hexdigest())
    conn.send(str(pass2_hash.hexdigest()).encode())

    pass2_reply = conn.recv(1024).decode()
    print(pass2_reply)
    pass1_reply = conn.recv(1024).decode()
    print(pass1_reply)
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

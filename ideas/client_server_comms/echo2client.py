#!/usr/bin/python

import socket


def Main():
    host = '127.0.0.1'
    port = 5001

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input("please enter a message, q to quit: ")

    while message != 'q':
        mySocket.send(message.encode())
        print('waiting for reply...')
        data = mySocket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input("please enter a message, q to quit!: ")

    mySocket.close()


if __name__ == '__main__':
    Main()

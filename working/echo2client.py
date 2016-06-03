#!/usr/bin/python
# working
# V1.1
# LOCATATED ON PI
# when running voice, check run location or file errors
# add functions to reply to server from pi eg run commands
import socket
import re
from modules.Voice import think


def main():
    try:
        host = '127.0.0.1'
        port = 5001
        sock = socket.socket()
        sock.connect((host, port))
        username = 'jonas'
        password1 = ''
        password2 = ''
        name = sock.recv(1024).decode()
        print(name)
        if name == username:
            print("User '{0}' logged in.".format(name))
            sock.send('Hello Dave...'.encode())
            pass1_hash = sock.recv(1024).decode()
            pass2_hash = sock.recv(1024).decode()
            print(pass1_hash)
            print(pass2_hash)
        else:
            sock.send('Incorrect Username!'.encode())
        message = input("please enter a message, :quit to quit: ")
        while message != ':quit':
            sock.send(message.encode())
            print('waiting for reply...')
            data = sock.recv(1024).decode()
            print('Received from server: ' + data)
            searchpattern = re.search(r'say', data, re.M | re.I)
            if searchpattern:
                print("found '{0}' in '{1}'".format(searchpattern.group(), data))
                text = data.split('say')
                print('saying...', text[1])
                think(text[1])
            message = input("please enter a message, :quit to quit...: ")
        sock.close()
    except ConnectionRefusedError:
        print('Server connection refused, start Server or check ports...')


if __name__ == '__main__':
    main()

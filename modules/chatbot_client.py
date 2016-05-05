

def client():
    import socket
    host = "localhost"
    port = 1024
    addr = (host, port)
    flag = True
    username = input('username : ')
    bot = 'Pibot'

    print('username : ', username)
    print('bot      : ', bot)

    data_in = ''

    while flag:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(addr)
        client_socket.sendall((bytes(username + chr(0) + bot + chr(0) + data_in + chr(0), 'UTF-8')))
        data_out = client_socket.recv(80)
        # print(data_out)
        x = data_out.decode("UTF-8")
        # print(x)
        print("{0} says: {1}".format(bot, x))
        data_in = input('>> ')
        print("sending '{0}' to {1}".format(data_in, bot))
        if ':exit' in data_in:
            break

        client_socket.close()


client()

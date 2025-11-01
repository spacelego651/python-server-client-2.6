"""Eyal Kahanovich
   a client connection for the server """


import socket

MAX_PACKET = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the server
try:
    my_socket.connect(('127.0.0.1', 2976))
    while True:
        request = input('enter your request (use only four chars) \n' )
        while len(request) != 4:
            print('the request is not valid')
            request = input('enter your request (use only four chars)\n')
        my_socket.send(request.encode())
        response = my_socket.recv(MAX_PACKET).decode()
        print(response)
        if request == 'EXIT':
            break
except socket.error as err:
    print('received socket error ' + str(err))




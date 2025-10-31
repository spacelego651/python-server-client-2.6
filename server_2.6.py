"""author: Eyal Kahanovich
   a server handling 4 commands: RAND, TIME, NAME and EXIT.
   handles 1 connection and logs events.
   date: 31.10.25 
"""



import socket
from datetime import datetime
import random
import logging

LOG_PATH = "/home/void_ek/projects/pythonserver/logfile.log"  

"""For some reason i cant input just LOG_PATH to the basicConfig, function so i added a full path decleration to the config, MUST BE CHANGED FOR DIFFERENT MACHINES"""

logging.basicConfig(
     filename=LOG_PATH,
     level=logging.INFO,
     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
     force=True
    )


QUEUE_LEN = 1
MAX_PACKET = 1024


server_name = "incredibly magnificent beautful smart and humble server"
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('0.0.0.0', 2976))
my_socket.listen(QUEUE_LEN)


def rand():
    """
    returns a random number between 1 and 10
    """
    return random.randint(1, 10)


def name():
    """
    the function returns the server name
    """
    return server_name


def main():
    while True:
        client_socket, client_address = my_socket.accept()
        try:
            while True:
                try:
                    request = client_socket.recv(MAX_PACKET).decode()
                    logging.info("server recieved request from client")
                    assert(request == "TIME" or request == "EXIT" or request == "RAND" or request == "NAME")
                    if request == 'TIME':
                        now = datetime.now()
                        readable_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        client_socket.send(readable_time.encode())
                    elif request == 'RAND':
                        client_socket.send(str(rand()).encode())
                    elif request == 'NAME':
                        client_socket.send(name().encode())
                    elif request == 'EXIT':
                        client_socket.close()
                        break
                    else:
                        client_socket.send("Not a command".encode())
                except socket.error as err:
                    logging.error("recieved socket error on client socket " + str(err))
                    print('received socket error on client socket' + str(err))
        except socket.error as err:
            logging.error('received socket error on server socket' + str(err))
            print('received socket error on server socket' + str(err))




if __name__ == "__main__":
    assert(name() == server_name)
    assert(rand() in range(1,11))
    main()
    



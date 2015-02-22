__author__ = 'william'

import socket
import time
import EmployeeManager
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2222

server_socket.bind((host, port))
server_socket.listen(1)

print('Awaiting connection...')
client_socket, addr = server_socket.accept()

print('Connection established...')
current_time = time.ctime(time.time())
msg = '[{}] You are connected to the server!'.format(current_time)
client_socket.send(msg.encode('utf-8'))

while True:
    client_data = client_socket.recv(1024)
    d = client_data.decode('utf-8')
    tokens = d.split(",")
    if tokens[0] == 'list':
        enc = EmployeeManager.listEmployees()
        client_socket.send(enc.encode('utf-8'))
        continue

    elif tokens[0] == 'search':
        enc = EmployeeManager.searchEmployee(tokens[1].decode('utf-8'))
        client_socket.send(enc.encode('utf-8'))
        continue


    elif tokens[0] == 'insert':
        print(tokens[1])
        EmployeeManager.insertEmployee(tokens[1])
        continue

    elif tokens[0] == 'edit':
        EmployeeManager.editEmployee(tokens[1], tokens[2])
        continue

    elif tokens[0] == "unique":
        enc = EmployeeManager.findValue(tokens[1].decode('utf-8'))
        client_socket.send(enc.encode('utf-8'))
        continue



    print('Closing connection with the client...')
    client_socket.close()





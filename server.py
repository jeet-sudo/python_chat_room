#server side
import time, socket, sys
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080
new_socket.bind((host_name, port))
print( "connected!")
print(" your IP: ", s_ip)
name = input('Enter your name: ')
new_socket.listen(1) 
conn, add = new_socket.accept()
print("Received connection ", add[0])
print('Connection Established : ',add[0])
client = (conn.recv(1024)).decode()
print(client + 'connected.')
conn.send(name.encode())
while True:
    message = input('me')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
#by jeet parmar 
#follow me on insta @tech_jwala_

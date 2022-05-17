import socket

HOST = socket.gethostbyname(socket.gethostname())
# HOST = 'localhost'
print(f"Host name: {HOST} \n")
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
client.send(bytes("This is a message".encode('utf-8')))
print(client.recv(1024))

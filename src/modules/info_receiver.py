import socket

HOST = socket.gethostbyname(socket.gethostname())
# HOST = 'localhost'
print(f"Host name: {HOST} \n")
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(4)
while True:
    print("Waiting for connection . . .")
    client,addr = server.accept()
    print(f"Connected to {addr} \n")
    message = client.recv(1024).decode('utf-8')
    print(f"message from client: {message} \n")
    client.send(f"Message recieved with message: {message}".encode('utf-8'))
    client.close()
    print(f"Connection with {addr} closed \n".decode('utf-8'))
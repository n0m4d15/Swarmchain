import socket
import json_load
HOST = socket.gethostbyname(socket.gethostname())
# HOST = 'localhost'
print(f"Host name: {HOST} \n")
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
loaded_data = json_load.data_load()
if loaded_data["inst_id"] == "NOID":
    client.send(bytes("Invalid Instruction ID".encode('utf-8')))
client.send(bytes(str(loaded_data).encode('utf-8')))
print(client.recv(1024))

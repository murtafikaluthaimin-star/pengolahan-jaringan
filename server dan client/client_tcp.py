# client.py
import socket

server_ip = '10.42.2.142'  # IP server
port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))
print(f"[CLIENT] Terhubung ke server {server_ip}:{port}")

while True:
    pesan = input("Client: ")
    client_socket.send(pesan.encode())

    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

client_socket.close()
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

while True:
    msg = input("You: ")
    client.send(msg.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print("Server:", response)

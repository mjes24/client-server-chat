import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)
print("Server is running and waiting for a connection...")

conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode("utf-8")
    if not data:
        break
    print("Client:", data)
    conn.send(f"Received: {data}".encode("utf-8"))

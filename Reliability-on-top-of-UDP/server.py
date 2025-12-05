from virtual_socket import VirtualSocket

sock = VirtualSocket()
sock.bind(('localhost', 5005))

print("Server is listening on port 5005...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data.decode(errors='replace')} from {addr}")
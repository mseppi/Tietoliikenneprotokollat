import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    text = input("Enter message to send: ")
    sock.sendto(text.encode(), ('localhost', 5005))
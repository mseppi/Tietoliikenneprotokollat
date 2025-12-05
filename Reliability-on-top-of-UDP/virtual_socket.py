import socket
import random
import time

class VirtualSocket:
    def __init__(self, loss_probability=0.2, delay_probability=0.2, max_delay=0.5, bit_error_probability=0.2):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.loss_probability = loss_probability
        self.delay_probability = delay_probability
        self.max_delay = max_delay
        self.bit_error_probability = bit_error_probability
        
    def sendto(self, data, addr):
        self.sock.sendto(data, addr)

    def recvfrom(self, bufsize):
        while True:
            data, addr = self.sock.recvfrom(bufsize)
            if random.random() < self.loss_probability:
                print("Packet lost")
                continue

            if random.random() < self.delay_probability:
                delay = random.uniform(0, self.max_delay)
                print(f"Packet delayed by {delay:.2f} seconds")
                time.sleep(delay)

            if random.random() < self.bit_error_probability:
                data = self.biterror(data)

            return data, addr

    def bind(self, addr):
        self.sock.bind(addr)

    def biterror(self, data):
        if len(data) == 0:
            return data
        byte_index = random.randint(0, len(data) - 1)
        bit_index = random.randint(0, 7)
        corrupted_byte = bytearray(data)
        corrupted_byte[byte_index] ^= 1 << bit_index
        return bytes(corrupted_byte)
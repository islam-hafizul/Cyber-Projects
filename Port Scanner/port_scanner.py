import socket
from threading import Thread, Lock
from queue import Queue

open_ports = []
print_lock = Lock()  # Thread-safe print lock

def scan_port(ip, port):
   try:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.settimeout(1)
       result = s.connect_ex((ip, port))
       with print_lock:
           if result == 0:
               open_ports.append(port)
               print(f"Port {port} is open")
           else:
               print(f"Port {port} is closed", end="\r")
       s.close()
   except(socket.timeout, socket.error):
       pass

def worker(ip, queue):
   while not queue.empty():
       port = queue.get()
       scan_port(ip, port)
       queue.task_done()

def main():
   target = input("Enter the target IP or hostname: ")
   ip = socket.gethostbyname(target)
   print(f"Scanning Target: {ip}")
   
   queue = Queue()
   for port in range(1, 1025): 
       queue.put(port)
   
   threads = []
   for _ in range(50): 
       thread = Thread(target=worker, args=(ip, queue))
       thread.daemon = True
       thread.start()
       threads.append(thread)
   queue.join() 
   print("The open ports are:", sorted(open_ports))

if __name__ == "__main__":
   main()
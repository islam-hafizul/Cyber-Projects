import socket
from threading import Thread, Lock
from queue import Queue
import time

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
   
   port_range = input("Enter port range (default 1-1024): ").strip()
   if port_range:
        start, end = map(int, port_range.split('-'))
   else:
        start, end = 1, 1025
   
   queue = Queue()
   for port in range(start, end): 
       queue.put(port)
   
   thread_count = input("Enter thread count (default 50): ").strip()
   thread_count = int(thread_count) if thread_count else 50

   start_time = time.time()

   threads = []
   for _ in range(thread_count): 
       thread = Thread(target=worker, args=(ip, queue))
       thread.daemon = True
       thread.start()
       threads.append(thread)
   queue.join() 
   
   print(f"\nScan complete in ~{time.time() - start_time:.2f} seconds")
   print("The open ports are:", sorted(open_ports))

if __name__ == "__main__":
   main()
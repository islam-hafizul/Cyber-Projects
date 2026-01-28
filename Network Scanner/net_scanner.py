import socket
import subprocess
import sys
import threading
from queue import Queue
from datetime import datetime
from typing import List, Dict, Tuple
import argparse
import ipaddress
from scapy.all import ARP, Ether, srp, ICMP, IP, TCP, sr1
from scapy.config import conf
    
conf.verb = 0  # Reduce Scapy verbosity

class NetworkScanner:
    def __init__(self, timeout: int = 2):
        self.timeout = timeout
        self.results = []
        self.scan_start_time = None
        
    def get_local_ip(self) -> str:
        try:
            # Create a dummy socket to get local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception:
            return "127.0.0.1"
    
    def get_network_range(self, ip: str = None) -> str:
        if not ip:
            ip = self.get_local_ip()
        
        # Convert IP to network (assuming /24 subnet)
        network_addr = ".".join(ip.split('.')[:3]) + ".0/24"
        return network_addr
    
    def arp_scan(self, network: str = None) -> List[Dict]:
        if not network:
            network = self.get_network_range()
        
        print(f"[*] Scanning network: {network}")
        
        # Create ARP request packet
        arp = ARP(pdst=network)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        try:
            # Send packet and receive responses
            result = srp(packet, timeout=self.timeout, verbose=False)[0]
            
            hosts = []
            for sent, received in result:
                hosts.append({
                    'ip': received.psrc,
                    'mac': received.hwsrc,
                    'hostname': self.get_hostname(received.psrc)
                })
            
            return hosts
            
        except Exception as e:
            print(f"[!] ARP Scan Error: {e}")
            return []
    
    # Ping sweep to discover active hosts 
    def ping_sweep(self, network: str = None, count: int = 1) -> List[str]:
        if not network:
            network = self.get_network_range()
        
        # Parse network range
        network_obj = ipaddress.ip_network(network, strict=False)
        active_hosts = []
        
        print(f"[*] Ping sweeping {network} ({network_obj.num_addresses} addresses)")
        
        def ping_host(ip):
            try:
                # Send ICMP echo request
                packet = IP(dst=str(ip))/ICMP()
                response = sr1(packet, timeout=1, verbose=False)
                
                if response:
                    return str(ip)
            except:
                pass
            return None
        
        # Scan all hosts in network
        for ip in network_obj.hosts():
            host = ping_host(ip)
            if host:
                active_hosts.append(host)
                print(f"[+] Host alive: {host}")
        
        return active_hosts
    
    # Scan for open ports on a target host
    def scan_ports(self, target: str, ports: List[int] = None) -> List[int]:
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389] # common ports
        
        open_ports = []
        
        print(f"[*] Scanning {target} on {len(ports)} ports")
        
        # Checks simngle port
        def scan_port(port): 
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((target, port))
                sock.close()
                
                if result == 0:
                    return port
            except:
                pass
            return None
        
        # Scan each port
        for port in ports:
            open_port = scan_port(port)
            if open_port:
                open_ports.append(open_port)
                service = self.get_service_name(port)
                print(f"[+] Port {port}/TCP open - {service}")
        
        return open_ports
    
    def get_hostname(self, ip: str) -> str:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return "Unknown"
    
    def get_service_name(self, port: int) -> str:
        services = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            135: "MSRPC",
            139: "NetBIOS",
            143: "IMAP",
            443: "HTTPS",
            445: "SMB",
            3389: "RDP",
            3306: "MySQL",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB"
        }
        return services.get(port, "Unknown")
    
    def scan_host(self, target: str) -> Dict:
        print(f"\n{'='*50}")
        print(f"Scanning host: {target}")
        print(f"{'='*50}")
        
        result = {
            'target': target,
            'hostname': self.get_hostname(target),
            'timestamp': datetime.now().isoformat(),
            'ports': []
        }
        
        print(f"[*] Hostname: {result['hostname']}")
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]
        open_ports = self.scan_ports(target, common_ports)
        
        if open_ports:
            result['ports'] = open_ports
            print(f"\n[*] Open ports: {', '.join(map(str, open_ports))}")
        else:
            print("\n[*] No open ports found on common services")
        
        return result
    
    # Main scan method
    def run_scan(self, scan_type: str = "discover", target: str = None):
        self.scan_start_time = datetime.now()
        
        print(f"\n{'='*60}")
        print("NETWORK SCANNER")
        print(f"{'='*60}")
        print(f"Started: {self.scan_start_time}")
        print(f"Scan type: {scan_type}")
        if target:
            print(f"Target: {target}")
        print(f"{'='*60}\n")
        
        # Discover all hosts in network
        if scan_type == "discover":
            hosts = self.arp_scan()
            
            if hosts:
                print(f"\n{'='*60}")
                print(f"DISCOVER RESULTS ({len(hosts)} hosts found)")
                print(f"{'='*60}")
                
                for i, host in enumerate(hosts, 1):
                    print(f"{i}. IP: {host['ip']:15} MAC: {host['mac']:17} Hostname: {host['hostname']}")
            else:
                print("\n[!] No hosts found")
        
        # Ping sweep
        elif scan_type == "ping":
            active_hosts = self.ping_sweep()
            print(f"\n[+] Found {len(active_hosts)} active hosts")
        
        # Port scan single host
        elif scan_type == "portscan" and target:
            self.scan_host(target)
        
        else:
            print("[!] Invalid scan type or missing target")
            print("Available scan types: discover, ping, portscan")
        
        # Calculate scan duration
        scan_duration = datetime.now() - self.scan_start_time
        print(f"\n{'='*60}")
        print(f"Scan completed in {scan_duration}")
        print(f"{'='*60}")

def main():
    parser = argparse.ArgumentParser(
        description="Simple Network Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s discover          # Discover all hosts in network
  %(prog)s ping              # Ping sweep network
  %(prog)s portscan 192.168.1.10  # Scan ports on specific host
  
  # Custom port range:
  python scanner.py --ports 22,80,443 portscan 192.168.1.1
        """
    )
    
    parser.add_argument("scan_type", 
                       choices=["discover", "ping", "portscan"],
                       help="Type of scan to perform")
    
    parser.add_argument("target", nargs="?", 
                       help="Target IP for portscan (required for portscan)")
    
    parser.add_argument("-p", "--ports", 
                       help="Comma-separated list of ports (e.g., 80,443,8080)")
    
    parser.add_argument("-t", "--timeout", type=int, default=2,
                       help="Timeout in seconds (default: 2)")
    
    parser.add_argument("--network", 
                       help="Network range (e.g., 192.168.1.0/24)")
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.scan_type == "portscan" and not args.target:
        parser.error("portscan requires a target IP address")
    
    # Create scanner instance
    scanner = NetworkScanner(timeout=args.timeout)
    
    # Parse ports if provided
    ports = None
    if args.ports:
        try:
            ports = [int(p) for p in args.ports.split(",")]
        except ValueError:
            print("[!] Invalid port list. Use comma-separated numbers.")
            sys.exit(1)
    
    # Run appropriate scan
    if args.scan_type == "portscan":
        if ports:
            print(f"[*] Scanning custom ports: {ports}")
            scanner.scan_ports(args.target, ports)
        else:
            scanner.scan_host(args.target)
    else:
        scanner.run_scan(args.scan_type, args.network)

if __name__ == "__main__":
    # Check for root privileges (required for ARP scanning)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        import os
        if os.geteuid() != 0:
            print("\n[!] Warning: Some features may require root privileges")
            print("   Try: sudo python scanner.py discover\n")
    
    main()
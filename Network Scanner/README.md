# Simple Network Scanner

A lightweight network scanner for discovering hosts and scanning ports.

## Features
- ARP scanning for host discover
- Ping sweep for active hosts
- TCP port scanning
- Hostname resolution
- Common service detection

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner

# Install dependencies
pip install -r requirements.txt
```
## Usage
Discover all hosts in your network:

```bash
# On Linux/Mac (requires sudo for ARP):
sudo python net_scanner.py discover

# On Windows (as Administrator):
python net_scanner.py discover
```
### Ping sweep:

```bash
python net_scanner.py ping
```
### Scan specific host:

```bash
python net_scanner.py portscan 192.168.1.1
```
### Scan custom ports:

```bash
python net_scanner.py --ports 22,80,443,8080 portscan 192.168.1.10
```
### Specify network range:

```bash
python net_scanner.py --network 10.0.0.0/24 discover
```
Examples
```text
$ sudo python net_scanner.py discover

============================================================
NETWORK SCANNER
============================================================
Started: 2024-01-15 10:30:00
Scan type: discover
============================================================

[*] Scanning network: 192.168.1.0/24
[+] Host alive: 192.168.1.1 (Router)
[+] Host alive: 192.168.1.100 (My-PC)

============================================================
DISCOVER RESULTS (2 hosts found)
============================================================
1. IP: 192.168.1.1    MAC: aa:bb:cc:dd:ee:ff    Hostname: router.local
2. IP: 192.168.1.100  MAC: 11:22:33:44:55:66    Hostname: mypc.local
```
## Requirements
- Python 3.6+
- Scapy
- Colorama (optional, for colored output)

## Legal Notice
Only scan networks you own or have permission to scan. Unauthorized scanning may be illegal.

## License
MIT

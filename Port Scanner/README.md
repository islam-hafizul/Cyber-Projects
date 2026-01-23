# Port Scanner

A fast and efficient multi-threaded port scanner written in Python that identifies open and closed ports on a target network host.

## Features

- **Multi-threaded scanning**: Uses 50 concurrent threads for faster port scanning
- **Port range support**: Scans ports 1-1024 (common ports)
- **Hostname/IP resolution**: Accepts both IP addresses and hostnames as targets
- **Thread-safe output**: Uses locks to ensure clean console output
- **Timeout handling**: Each port check times out after 1 second to avoid hanging
- **Lightweight**: Minimal dependencies (uses only built-in Python libraries)

## Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## Usage

```bash
python port_scanner.py
```

When prompted, enter the target IP address or hostname:
```
Enter the target IP or hostname: example.com
```

The scanner will then display the status of each port:
```
Scanning Target: 93.184.216.34
Port 80 is open
Port 443 is open
```

## How It Works

1. **Input**: Accepts a target IP address or hostname from the user
2. **Resolution**: Converts hostname to IP address using `socket.gethostbyname()`
3. **Queue Creation**: Creates a queue with ports 1-1024 to be scanned
4. **Threading**: Spawns 50 worker threads that process ports from the queue
5. **Scanning**: Each thread attempts to connect to ports on the target
6. **Collection**: Open ports are stored in a list as they're found
7. **Results**: After completion, all open ports are displayed sorted

## Technical Details

- **Connection Method**: TCP connect scan using `socket.connect_ex()`
- **Timeout**: 1 second per port connection attempt
- **Thread Safety**: Uses `Lock()` to prevent output race conditions during printing
- **Daemon Threads**: Worker threads run as daemon threads for clean shutdown
- **Queue-based Distribution**: Ports are distributed among threads via a `Queue` object
- **Result Collection**: Open ports are stored in a list and sorted before final display
- **Exception Handling**: Catches `socket.timeout` and `socket.error` exceptions specifically

## Notes

- This tool requires network access to the target
- Some networks or firewalls may block or rate-limit port scanning
- Scanning ports on systems without permission may be illegal
- Use responsibly and ethically
- Performance may vary based on network conditions and host responsiveness

## Customization

To modify the scanner behavior, you can adjust:

- **Port range**: Change `range(1, 1025)` to scan different ports
- **Thread count**: Modify `for _ in range(50)` to use more/fewer threads
- **Timeout duration**: Change `sock.settimeout(1)` to increase/decrease timeout

## Example

```bash
$ python port_scanner.py
Enter the target IP or hostname: 192.168.1.1
Scanning Target: 192.168.1.1
Port 22 is open
Port 80 is open
Port 443 is open
The open ports are: [22, 80, 443]
```

## Disclaimer

This tool is for educational and authorized security testing purposes only. Unauthorized port scanning may violate laws and regulations. Always obtain proper permission before scanning any system or network.

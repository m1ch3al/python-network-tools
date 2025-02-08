import socket
from concurrent.futures import ThreadPoolExecutor

port_services = {
    20: "FTP (Data Transfer)",
    21: "FTP (Command Control)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Email Routing)",
    53: "DNS (Domain Name System)",
    67: "DHCP (Dynamic Host Configuration Protocol) - Server",
    68: "DHCP (Dynamic Host Configuration Protocol) - Client",
    69: "TFTP (Trivial File Transfer Protocol)",
    80: "HTTP (HyperText Transfer Protocol)",
    110: "POP3 (Post Office Protocol)",
    119: "NNTP (Network News Transfer Protocol)",
    123: "NTP (Network Time Protocol)",
    135: "Microsoft RPC",
    137: "NetBIOS (Name Service)",
    138: "NetBIOS (Datagram Service)",
    139: "NetBIOS (Session Service)",
    143: "IMAP (Internet Message Access Protocol)",
    161: "SNMP (Simple Network Management Protocol)",
    162: "SNMPTRAP (SNMP Trap)",
    194: "IRC (Internet Relay Chat)",
    389: "LDAP (Lightweight Directory Access Protocol)",
    443: "HTTPS (HTTP Secure)",
    445: "Microsoft-DS (Active Directory, Windows Shares)",
    465: "SMTPS (SMTP SSL/TLS)",
    514: "Syslog",
    515: "LPD (Line Printer Daemon)",
    587: "SMTP (Email Submission)",
    636: "LDAPS (Secure LDAP)",
    989: "FTPS (Data)",
    990: "FTPS (Control)",
    993: "IMAPS (Secure IMAP)",
    995: "POP3S (Secure POP3)",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Monitor",
    1521: "Oracle SQL",
    1723: "PPTP (Point-to-Point Tunneling Protocol)",
    2049: "NFS (Network File System)",
    2082: "cPanel (Web Hosting Panel)",
    2083: "cPanel Secure (Web Hosting Panel Secure)",
    3306: "MySQL Database",
    3389: "RDP (Remote Desktop Protocol)",
    5432: "PostgreSQL Database",
    5900: "VNC (Virtual Network Computing)",
    6379: "Redis Database",
    8080: "HTTP Alternative (Often Proxy/Custom Web Service)",
    8443: "HTTPS Alternative (Often Used for Web Services)",
    9090: "Openfire Administration Console",
    11211: "Memcached",
    25565: "Minecraft Server",
    27017: "MongoDB",
    31337: "Back Orifice (Commonly Associated with Malware)",
    49152: "Reserved (Start of Ephemeral Ports)",
}


def show_banner():
    banner = """
 ######                             #####                                            
 #     #  ####  #####  #####       #     #  ####    ##   #    # #    # ###### #####  
 #     # #    # #    #   #         #       #    #  #  #  ##   # ##   # #      #    # 
 ######  #    # #    #   #   #####  #####  #      #    # # #  # # #  # #####  #    # 
 #       #    # #####    #               # #      ###### #  # # #  # # #      #####  
 #       #    # #   #    #         #     # #    # #    # #   ## #   ## #      #   #  
 #        ####  #    #   #          #####   ####  #    # #    # #    # ###### #    # 
                                                                                     
                                                                            by m1ch3al\n\n                                                      
    """
    print(banner)



# Function to check if a port is open
def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    if result == 0:
        return port
    else:
        return None


# Function to scan a range of ports
def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port = future.result()
            if port is not None:
                open_ports.append(port)

    return open_ports


def print_open_ports(opened_ports):
    for single_port in opened_ports:
        if single_port in port_services.keys():
            print("{} : {}".format(single_port, port_services[single_port]))
        else:
            print("{} : Unknown service".format(single_port))


def main():
    show_banner()
    target = input("Enter the target IP or FQDN: ")
    start_port = input("Enter the start port (min value is 1): ")
    end_port = input("Enter the end port (max value is 65535): ")
    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except ValueError as ex:
        print("\n[ERROR] Invalid characters found: Ports entered must be integers")
        print(" Exception: {}".format(ex))
        exit(-1)

    print("Checking port(s)....")
    if 1 <= start_port < 65536 and 1 <= end_port < 65536 and start_port < end_port:
        open_ports = port_scanner(target, start_port, end_port)
        print("Scan complete...")
        if open_ports:
            print("Found {} open ports on {}".format(len(open_ports), target))
            print_open_ports(open_ports)
        else:
            print("No open ports found on {}".format(target))
    else:
        print(" Invalid port range! Ensure the following:")
        print("  - start port and end port must be in the range [1, 65535].")
        print("  - start port must be less than end port.")


if __name__ == "__main__":
    main()

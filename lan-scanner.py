import socket
import subprocess
import ipaddress
import sys
import threading
import time
from queue import Queue

scan_result = Queue()
threads = []

def show_banner():
    banner = """

██       █████  ███    ██       ███████  ██████  █████  ███    ██ ███    ██ ███████ ██████  
██      ██   ██ ████   ██       ██      ██      ██   ██ ████   ██ ████   ██ ██      ██   ██ 
██      ███████ ██ ██  ██ █████ ███████ ██      ███████ ██ ██  ██ ██ ██  ██ █████   ██████  
██      ██   ██ ██  ██ ██            ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
███████ ██   ██ ██   ████       ███████  ██████ ██   ██ ██   ████ ██   ████ ███████ ██   ██ 

by m1ch3al\n"""
    print(banner)


def get_dns_by_ip(ip_address):
    try:
        host_name, alias_list, ip_list = socket.gethostbyaddr(ip_address)
        return host_name
    except socket.herror as e:
        return None


def ping(address):
    global scan_result
    try:
        result = subprocess.run(["ping", "-c", "2", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            hostname = get_dns_by_ip(address)
            if hostname is not None:
                scan_result.put_nowait("{} ({})".format(address, hostname))
            else:
                scan_result.put_nowait("{}".format(address))
            return True
        else:
            return False
    except Exception as e:
        return False


def scan_lan(network):
    global threads
    try:
        net = ipaddress.ip_network(network, strict=False)
        print("Starting LAN-Scan into: {}\nPLEASE WAIT...".format(network))
        for ip in net.hosts():
            ip_str = str(ip)
            ping_thread = threading.Thread(target=ping, args=(ip_str,))
            ping_thread.daemon = True
            threads.append(ping_thread)
            ping_thread.start()
    except ValueError as e:
        print("Error in the specified network: {}".format(e))


def show_results(lan_information):
    print("\n[LAN-SCAN completed]")
    print("Reachable network object(s): {}".format(lan_information.qsize()))
    while not lan_information.empty():
        reachable_item = lan_information.get_nowait()
        print(" + {}".format(reachable_item))
    print("")


def validate_cidr(ip_string):
    try:
        network = ipaddress.ip_network(ip_string, strict=False)
        return True
    except ValueError as e:
        return False

def quitting():
    print("Incorrect or missing argument(s)")
    print("Usage : python lan-scanner.py 192.168.1.0/24")
    sys.exit(-1)


def main():
    global threads
    global scan_result
    show_banner()

    if len(sys.argv) != 2:
        quitting()
    else:
        if validate_cidr(sys.argv[1]) is False:
            quitting()

        scan_lan(sys.argv[1])
        time.sleep(2)
        for thread in threads:
            thread.join()
        show_results(scan_result)


if __name__ == "__main__":
    main()

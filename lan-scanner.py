import subprocess
import ipaddress
import threading

# need to be finished

def show_banner():
    banner = """

██       █████  ███    ██       ███████  ██████  █████  ███    ██ ███    ██ ███████ ██████  
██      ██   ██ ████   ██       ██      ██      ██   ██ ████   ██ ████   ██ ██      ██   ██ 
██      ███████ ██ ██  ██ █████ ███████ ██      ███████ ██ ██  ██ ██ ██  ██ █████   ██████  
██      ██   ██ ██  ██ ██            ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
███████ ██   ██ ██   ████       ███████  ██████ ██   ██ ██   ████ ██   ████ ███████ ██   ██ 

by m1ch3al\n\n
    """
    print(banner)

def ping(address):
    try:
        result = subprocess.run(["ping", "-c", "2", address], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        if result.returncode == 0:
            print("ACTIVE : {}".format(address))
            return True
        else:
            return False
    except Exception as e:
        return False

def scan_lan(network):
    try:
        # Usa il modulo ipaddress per analizzare la sottorete (es. 192.168.1.0/24)
        net = ipaddress.ip_network(network, strict=False)
        print(f"[INFO] Inizio scansione della rete: {network}")

        # Scansiona ogni indirizzo IP nella rete
        active_hosts = []
        for ip in net.hosts():  # Esclude gli indirizzi broadcast e network
            ip_str = str(ip)
            ping_thread = threading.Thread(target=ping, args=(ip_str,))
            ping_thread.daemon = True
            ping_thread.start()
        #print(f"\n[INFO] Scansione completata. Host attivi trovati: {len(active_hosts)}")
        #return active_hosts
    except ValueError as e:
        print(f"Errore nella rete specificata: {e}")
        return []


def main():
    network = input("Insert subnet to scan (es. 192.168.1.0/24): ")
    active_hosts = scan_lan(network)
    #print("\nHost attivi trovati:")
    #for host in active_hosts:
    #    print(host)

if __name__ == "__main__":
    main()

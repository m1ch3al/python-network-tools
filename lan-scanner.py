import os
import platform


def ping_host(ip_address):
    """
    Esegue il ping di un singolo indirizzo IP.
    Ritorna True se l'host è raggiungibile, False altrimenti.
    """
    # Determina l'opzione del comando 'ping' in base al sistema operativo
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Costruisce il comando di sistema per il ping
    command = f"ping {param} 1 -w 1 {ip_address}"  # 1 tentativo, timeout 1 secondo

    # Esegui il comando e controlla il codice di ritorno
    return os.system(command) == 0


def ping_range(start_ip, end_ip):
    """
    Esegue il ping su uno spazio di indirizzi IP da start_ip a end_ip.
    Gli indirizzi vengono iterati in ordine progressivo.
    """

    def ip_to_list(ip):
        return list(map(int, ip.split('.')))

    def list_to_ip(ip):
        return '.'.join(map(str, ip))

    def increment_ip(ip):
        ip[3] += 1
        for i in range(3, 0, -1):
            if ip[i] > 255:
                ip[i] = 0
                ip[i - 1] += 1
        return ip

    # Trasforma gli IP di input in liste per il calcolo
    current_ip = ip_to_list(start_ip)
    end_ip_list = ip_to_list(end_ip)

    # Esegui il ping su tutta la gamma
    while current_ip <= end_ip_list:
        ip_str = list_to_ip(current_ip)
        is_reachable = ping_host(ip_str)

        # Stampa il risultato del ping
        if is_reachable:
            print(f"[+] Host {ip_str} is reachable")
        else:
            print(f"[-] Host {ip_str} is not reachable")

        # Incrementa l'indirizzo IP corrente
        current_ip = increment_ip(current_ip)


def main():
    # Intervallo di indirizzi IP
    start_ip = "192.168.1.1"
    end_ip = "192.168.1.254"

    print(f"Pinging IP range from {start_ip} to {end_ip}...\n")
    ping_range(start_ip, end_ip)

if __name__ == "__main__":
    main()

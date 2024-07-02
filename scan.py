import socket

def scan_ports(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ports = range(1, 1025)
    scan_ports(target, ports)

import socket

def scan_all_ports(host):
    print(f"Сканування всіх портів на {host}...")
    for port in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Порт {port} відкритий")

host = "127.0.0.1"
scan_all_ports(host)

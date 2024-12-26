import socket

def scan_one_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Порт {port} відкритий")
        else:
            print(f"Порт {port} закритий")

host = "127.0.0.1"  
port = 80  
scan_one_port(host, port)

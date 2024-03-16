
import socket

IP = input("Enter a host to scan: ")
Scan = socket.gethostbyname(IP)

for port in range(1, 65535):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = soc.connect_ex((Scan, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "Unknown"
        print("Port {}: Open - Service: {}".format(port, service))
    sock.close()

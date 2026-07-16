import socket

domains = ["www.google.com", "www.python.org", "notarealdomain12345.com"]
print("OSINT Domain Reconnaissance")

for d in domains:
    try:
        ip = socket.gethostbyname(d)
        print(f"{d:30s} -> {ip}")
    except socket.gaierror:
        print(f"{d:30s} -> Could not resolve (invalid/unreachable)")

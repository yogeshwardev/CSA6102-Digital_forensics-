# Create a sample simulated packet log so this runs standalone
with open("traffic.log", "w") as f:
    f.write("10.0.0.9 -> 10.0.0.5:22 SYN\n")
    f.write("10.0.0.9 -> 10.0.0.5:23 SYN\n")
    f.write("10.0.0.9 -> 10.0.0.5:25 SYN\n")
    f.write("10.0.0.9 -> 10.0.0.5:80 SYN\n")
    f.write("10.0.0.9 -> 10.0.0.5:443 SYN\n")
    f.write("10.0.0.20 -> 10.0.0.5:80 SYN\n")
    f.write("10.0.0.20 -> 10.0.0.5:80 ACK\n")

# Count distinct destination ports probed by each source IP
ports_by_source = {}
with open("traffic.log") as f:
    for line in f:
        parts = line.split()
        src = parts[0]
        dst_port = parts[2].split(":")[1]
        ports_by_source.setdefault(src, set()).add(dst_port)

print("Network traffic forensic analysis:")
for src, ports in ports_by_source.items():
    print(f" {src}: contacted {len(ports)} distinct port(s) -> {sorted(ports)}")
    if len(ports) >= 4:
        print(f" -> ALERT: {src} shows port-scanning behaviour")

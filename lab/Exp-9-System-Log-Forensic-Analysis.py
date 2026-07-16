import re
from collections import Counter

# Create the sample system log so the script runs standalone
with open("login_attempts.log", "w") as f:
    f.write("2026-07-08 09:00:01 LOGIN SUCCESS user=alice ip=10.0.0.5\n")
    f.write("2026-07-08 09:01:15 LOGIN FAILED user=admin ip=203.0.113.99\n")
    f.write("2026-07-08 09:01:20 LOGIN FAILED user=admin ip=203.0.113.99\n")
    f.write("2026-07-08 09:01:25 LOGIN FAILED user=admin ip=203.0.113.99\n")
    f.write("2026-07-08 09:01:30 LOGIN FAILED user=admin ip=203.0.113.99\n")
    f.write("2026-07-08 09:01:35 LOGIN FAILED user=admin ip=203.0.113.99\n")
    f.write("2026-07-08 09:02:00 LOGIN SUCCESS user=bob ip=10.0.0.8\n")

failed_by_ip = Counter()
with open("login_attempts.log") as f:
    for line in f:
        if "LOGIN FAILED" in line:
            match = re.search(r"ip=(\S+)", line)
            if match:
                failed_by_ip[match.group(1)] += 1

print("System log forensic analysis - failed logins by source IP:")
for ip, count in failed_by_ip.items():
    print(f" {ip}: {count} failed attempts")
    if count >= 5:
        print(f" -> Evidence of brute-force intrusion attempt from {ip}")

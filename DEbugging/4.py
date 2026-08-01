def detect_bruteforce(log_lines, threshold=5):
    ip_counts = {}

    for line in log_lines:
        if 'FAILED LOGIN' in line:
            parts = line.split()
            ip = parts[-1]

            ip_counts[ip] = ip_counts.get(ip, 0) + 1

    flagged = []

    for ip, count in ip_counts.items():
        if count >= threshold:
            flagged.append(ip)

    return flagged


log = [
    'FAILED LOGIN user=admin from 10.0.0.5',
    'FAILED LOGIN user=admin from 10.0.0.5',
    'FAILED LOGIN user=root from 10.0.0.5'
]

print(detect_bruteforce(log, threshold=2))
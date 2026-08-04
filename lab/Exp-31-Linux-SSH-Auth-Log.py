import re

AUTH_LINE_RE = re.compile(
    r"(?P<result>Accepted|Failed) password for (?P<user>\S+) from (?P<ip>[\d.]+) port (?P<port>\d+)"
)

def parse_auth_log(lines):
    """Parse raw auth.log lines into structured dicts."""
    entries = []
    for line in lines:
        match = AUTH_LINE_RE.search(line)
        if match:
            entries.append({
                "result": match.group("result"),
                "user": match.group("user"),
                "ip": match.group("ip"),
                "port": int(match.group("port")),
                "raw": line,
            })
    return entries

def flag_suspicious_logins(entries, trusted_ips):
    """Flag successful logins from untrusted IPs, especially for root."""
    flagged = []
    for e in entries:
        if e["result"] == "Accepted" and e["ip"] not in trusted_ips:
            severity = "HIGH" if e["user"] == "root" else "MEDIUM"
            flagged.append({**e, "severity": severity})
    return flagged

def test_experiment31():
    log_lines = [
        "Jan 15 08:00:01 server sshd[1001]: Accepted password for deploy from 10.0.0.5 port 51100 ssh2",
        "Jan 15 03:12:01 server sshd[1233]: Failed password for root from 198.51.100.23 port 51320 ssh2",
        "Jan 15 03:12:05 server sshd[1234]: Accepted password for root from 198.51.100.23 port 51322 ssh2",
    ]
    trusted_ips = {"10.0.0.5"}
    entries = parse_auth_log(log_lines)
    assert len(entries) == 3
    flagged = flag_suspicious_logins(entries, trusted_ips)
    assert len(flagged) == 1
    assert flagged[0]["user"] == "root"
    assert flagged[0]["ip"] == "198.51.100.23"
    assert flagged[0]["severity"] == "HIGH"
    print("Experiment 31: All test cases passed.")

test_experiment31()

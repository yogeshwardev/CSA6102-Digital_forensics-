from datetime import datetime
from collections import Counter

LOG_FMT = "%Y-%m-%d %H:%M:%S"

def build_baseline_ips(logs):
    """Return {user: most_common_ip} based on all log activity."""
    by_user = {}
    for entry in logs:
        by_user.setdefault(entry["user"], []).append(entry["ip"])
    return {user: Counter(ips).most_common(1)[0][0] for user, ips in by_user.items()}

def flag_anomalous_downloads(logs, business_start=8, business_end=20):
    baseline = build_baseline_ips(logs)
    flagged = []
    for entry in logs:
        if entry["action"] != "download":
            continue
        ts = datetime.strptime(entry["timestamp"], LOG_FMT)
        reasons = []
        if entry["ip"] != baseline.get(entry["user"]):
            reasons.append("IP differs from user baseline")
        if not (business_start <= ts.hour < business_end):
            reasons.append("Outside business hours")
        if reasons:
            flagged.append({**entry, "reasons": reasons})
    return flagged

def test_experiment37():
    logs = [
        {"user": "alice", "action": "view", "file": "roadmap.docx", "timestamp": "2026-03-01 10:00:00", "ip": "10.0.0.5"},
        {"user": "alice", "action": "view", "file": "budget.xlsx", "timestamp": "2026-03-02 11:00:00", "ip": "10.0.0.5"},
        {"user": "alice", "action": "download", "file": "report.pdf", "timestamp": "2026-03-03 14:00:00", "ip": "10.0.0.5"},
        {"user": "alice", "action": "download", "file": "customer_database.csv", "timestamp": "2026-03-05 02:15:00", "ip": "185.220.101.7"},
    ]
    flagged = flag_anomalous_downloads(logs)
    assert len(flagged) == 1
    assert flagged[0]["file"] == "customer_database.csv"
    assert "IP differs from user baseline" in flagged[0]["reasons"]
    assert "Outside business hours" in flagged[0]["reasons"]
    print("Experiment 37: All test cases passed.")

test_experiment37()

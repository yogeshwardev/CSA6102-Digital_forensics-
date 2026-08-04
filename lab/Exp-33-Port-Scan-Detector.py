from datetime import datetime, timedelta

PKT_FMT = "%Y-%m-%d %H:%M:%S"

def detect_port_scan(packets, port_threshold=10, window_seconds=30):
    """Detect (src_ip -> dst_ip) pairs that contact >= port_threshold
    distinct destination ports within window_seconds."""
    packets = sorted(packets, key=lambda p: datetime.strptime(p["timestamp"], PKT_FMT))
    by_pair = {}
    for p in packets:
        key = (p["src_ip"], p["dst_ip"])
        by_pair.setdefault(key, []).append(p)
    results = {}
    for key, pkts in by_pair.items():
        for i in range(len(pkts)):
            start = datetime.strptime(pkts[i]["timestamp"], PKT_FMT)
            end = start + timedelta(seconds=window_seconds)
            ports_in_window = {
                p["dst_port"] for p in pkts
                if start <= datetime.strptime(p["timestamp"], PKT_FMT) <= end
            }
            if len(ports_in_window) >= port_threshold:
                results[key] = {
                    "distinct_ports": len(ports_in_window),
                    "ports": sorted(ports_in_window),
                }
                break
    return results

def test_experiment33():
    packets = []
    base = datetime(2026, 3, 1, 10, 0, 0)
    for i, port in enumerate(range(20, 32)):
        packets.append({
            "src_ip": "203.0.113.99", "dst_ip": "10.0.0.10",
            "dst_port": port,
            "timestamp": (base + timedelta(seconds=2 * i)).strftime(PKT_FMT),
        })
    for i in range(5):
        packets.append({
            "src_ip": "10.0.0.20", "dst_ip": "10.0.0.30",
            "dst_port": 443,
            "timestamp": (base + timedelta(seconds=5 * i)).strftime(PKT_FMT),
        })
    results = detect_port_scan(packets, port_threshold=10, window_seconds=30)
    assert ("203.0.113.99", "10.0.0.10") in results
    assert results[("203.0.113.99", "10.0.0.10")]["distinct_ports"] >= 10
    assert ("10.0.0.20", "10.0.0.30") not in results
    print("Experiment 33: All test cases passed.")

test_experiment33()

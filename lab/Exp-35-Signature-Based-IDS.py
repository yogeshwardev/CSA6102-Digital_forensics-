SIGNATURES = [
    {"sid": 1000001, "name": "Possible SQL Injection", "pattern": "union select"},
    {"sid": 1000002, "name": "Directory Traversal Attempt", "pattern": "../../../etc/passwd"},
    {"sid": 1000003, "name": "Nmap Scripting Engine User-Agent", "pattern": "nmap scripting engine"},
]

def scan_payloads(packets, signatures=SIGNATURES):
    """packets: list of dicts with a 'payload' string field.
    Returns list of alerts: {packet_index, sid, name}."""
    alerts = []
    for idx, pkt in enumerate(packets):
        payload_lower = pkt["payload"].lower()
        for sig in signatures:
            if sig["pattern"] in payload_lower:
                alerts.append({
                    "packet_index": idx,
                    "sid": sig["sid"],
                    "name": sig["name"],
                })
    return alerts

def test_experiment35():
    packets = [
        {"payload": "GET /products?id=1 HTTP/1.1"},
        {"payload": "GET /login?user=admin' UNION SELECT username,password FROM users-- HTTP/1.1"},
        {"payload": "GET /download?file=../../../etc/passwd HTTP/1.1"},
    ]
    alerts = scan_payloads(packets)
    alert_indices = {a["packet_index"] for a in alerts}
    assert 0 not in alert_indices
    assert 1 in alert_indices
    assert 2 in alert_indices
    assert any(a["name"] == "Possible SQL Injection" for a in alerts)
    assert any(a["name"] == "Directory Traversal Attempt" for a in alerts)
    print("Experiment 35: All test cases passed.")

test_experiment35()

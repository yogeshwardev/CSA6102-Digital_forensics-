from datetime import datetime, timedelta

def parse_time(t):
    return datetime.strptime(t, "%Y-%m-%d %H:%M:%S")

def detect_bruteforce(events, threshold=5, window_minutes=2):
    """Detect brute-force login attempts: >= threshold failed logons (4625)
    for the same account within window_minutes, and report whether a
    successful logon (4624) followed."""
    events = sorted(events, key=lambda e: parse_time(e["timestamp"]))
    by_account = {}
    for e in events:
        by_account.setdefault(e["account"], []).append(e)
    results = {}
    for account, acc_events in by_account.items():
        failures = [e for e in acc_events if e["event_id"] == 4625]
        successes = [e for e in acc_events if e["event_id"] == 4624]
        flagged = False
        for i in range(len(failures)):
            window_start = parse_time(failures[i]["timestamp"])
            window_end = window_start + timedelta(minutes=window_minutes)
            count = sum(
                1 for f in failures
                if window_start <= parse_time(f["timestamp"]) <= window_end
            )
            if count >= threshold:
                flagged = True
                break

        if flagged:
            followed_by_success = bool(successes) and any(
                parse_time(s["timestamp"]) > parse_time(failures[-1]["timestamp"])
                for s in successes
            )
            results[account] = {
                "failed_attempts": len(failures),
                "followed_by_success": followed_by_success,
                "source_ips": sorted({f["source_ip"] for f in failures}),
            }
    return results

def test_experiment29():
    events = []
    base = datetime(2026, 1, 15, 3, 40, 0)
    for i in range(6):
        events.append({
            "event_id": 4625, "account": "Administrator",
            "timestamp": (base + timedelta(seconds=15 * i)).strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": "203.0.113.7",
        })
    events.append({
        "event_id": 4624, "account": "Administrator",
        "timestamp": (base + timedelta(seconds=100)).strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": "203.0.113.7",
    })
    events.append({
        "event_id": 4624, "account": "jsmith",
        "timestamp": "2026-01-15 09:00:00", "source_ip": "10.0.0.5",
    })
    results = detect_bruteforce(events)
    assert "Administrator" in results
    assert results["Administrator"]["failed_attempts"] == 6
    assert results["Administrator"]["followed_by_success"] is True
    assert results["Administrator"]["source_ips"] == ["203.0.113.7"]
    assert "jsmith" not in results
    print("Experiment 29: All test cases passed.")

test_experiment29()

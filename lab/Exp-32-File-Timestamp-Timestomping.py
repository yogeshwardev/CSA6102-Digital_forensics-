from datetime import datetime

TS_FMT = "%Y-%m-%d %H:%M:%S"

def detect_timestomping(file_meta, change_gap_minutes=60):
    """file_meta: {"modified", "accessed", "changed", "born"} as timestamp
    strings. Returns (is_suspicious: bool, reasons: list[str])."""
    m = datetime.strptime(file_meta["modified"], TS_FMT)
    a = datetime.strptime(file_meta["accessed"], TS_FMT)
    c = datetime.strptime(file_meta["changed"], TS_FMT)
    b = datetime.strptime(file_meta["born"], TS_FMT)
    reasons = []
    if m < b:
        reasons.append("Modified time is earlier than Born (creation) time")
    if a < b:
        reasons.append("Accessed time is earlier than Born (creation) time")
    gap_minutes = abs((c - m).total_seconds()) / 60
    if gap_minutes > change_gap_minutes and c > m:
        reasons.append(
            f"MFT Changed time is {gap_minutes:.0f} minutes after Modified time — "
            "metadata may have been altered after the fact"
        )
    return (len(reasons) > 0, reasons)

def test_experiment32():
    normal_file = {
        "born": "2026-01-10 09:00:00",
        "modified": "2026-01-10 09:05:00",
        "accessed": "2026-01-12 14:00:00",
        "changed": "2026-01-10 09:05:00",
    }
    tampered_file = {
        "born": "2026-02-01 12:00:00",
        "modified": "2020-01-01 00:00:00",
        "accessed": "2026-02-01 12:00:00",
        "changed": "2026-02-01 12:03:00",
    }
    is_susp1, reasons1 = detect_timestomping(normal_file)
    assert is_susp1 is False
    is_susp2, reasons2 = detect_timestomping(tampered_file)
    assert is_susp2 is True
    assert any("Modified time is earlier" in r for r in reasons2)
    print("Experiment 32: All test cases passed.")

test_experiment32()

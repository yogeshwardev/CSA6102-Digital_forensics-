def recover_deleted_messages(sms_table):
    """sms_table: list of dicts with is_deleted (bool) and overwritten (bool).
    Returns a list of rows that are deleted but still recoverable."""
    recoverable = [
        row for row in sms_table
        if row["is_deleted"] and not row["overwritten"]
    ]
    return recoverable

def summarize_table(sms_table):
    active = [r for r in sms_table if not r["is_deleted"]]
    recoverable = recover_deleted_messages(sms_table)
    lost = [r for r in sms_table if r["is_deleted"] and r["overwritten"]]
    return {"active": len(active), "recoverable": len(recoverable), "permanently_lost": len(lost)}

def test_experiment36():
    sms_table = [
        {"rowid": 1, "address": "+1-555-0101", "body": "See you at 6pm", "date": "2026-01-01", "is_deleted": False, "overwritten": False},
        {"rowid": 2, "address": "+1-555-0199", "body": "Transfer the funds now, delete after reading", "date": "2026-01-02", "is_deleted": True, "overwritten": False},
        {"rowid": 3, "address": "+1-555-0150", "body": "Old spam message", "date": "2025-06-01", "is_deleted": True, "overwritten": True},
    ]
    recoverable = recover_deleted_messages(sms_table)
    assert len(recoverable) == 1
    assert recoverable[0]["rowid"] == 2
    assert "Transfer the funds" in recoverable[0]["body"]
    summary = summarize_table(sms_table)
    assert summary == {"active": 1, "recoverable": 1, "permanently_lost": 1}
    print("Experiment 36: All test cases passed.")

test_experiment36()

import hashlib
import json

def acquire(path):
    with open(path, "rb") as f:
        return f.read()

def hash_data(data):
    return hashlib.sha256(data).hexdigest()

def verify_integrity(data, expected_hash):
    return hash_data(data) == expected_hash

def analyze(data, keyword: bytes):
    return keyword in data

def generate_report(case_id, file_hash, keyword_found):
    return {
        "case_id": case_id,
        "sha256": file_hash,
        "suspicious_keyword_found": keyword_found,
        "status": "Evidence Verified" if keyword_found else "No Match",
    }

evidence_path = "workflow_evidence.txt"
with open(evidence_path, "w") as f:
    f.write("Transfer $50000 to account 99881122 immediately, do not report.")

acquired_data = acquire(evidence_path)
evidence_hash = hash_data(acquired_data)
integrity_ok = verify_integrity(acquired_data, evidence_hash)
keyword_found = analyze(acquired_data, b"99881122")
report = generate_report("CASE-2026-014", evidence_hash, keyword_found)

print(json.dumps(report, indent=2))

def test_experiment27():
    assert integrity_ok is True, "Hash verification must succeed on unaltered evidence"
    assert keyword_found is True, "Analysis must detect the suspicious account number"
    assert report["status"] == "Evidence Verified"
    tampered = acquired_data.replace(b"50000", b"99999")
    assert verify_integrity(tampered, evidence_hash) is False, "Tampered evidence must fail hash verification"
    print("Experiment 27: All test cases passed.")

test_experiment27()

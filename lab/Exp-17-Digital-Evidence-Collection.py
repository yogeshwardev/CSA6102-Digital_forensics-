import os
import hashlib

evidence_dir = "digital_evidence"
os.makedirs(evidence_dir, exist_ok=True)
sample_evidence = {
    "email_log.txt": "From: attacker@mail.com\nTo: victim@mail.com\nSubject: Invoice\nPlease pay immediately.",
    "browser_history.txt": "http://malicious-site.com/login\nhttp://bank.com/transfer",
    "chat_message.txt": "Hey, did you send the file?",
    "system_log.txt": "2026-07-24 10:15:32 - USB device connected: E:\\",
}

for filename, content in sample_evidence.items():
    with open(os.path.join(evidence_dir, filename), "w") as f:
        f.write(content)

def catalog_evidence(folder):
    catalog = []
    for fname in sorted(os.listdir(folder)):
        path = os.path.join(folder, fname)
        stat = os.stat(path)
        with open(path, "rb") as f:
            data = f.read()
        catalog.append({
            "filename": fname,
            "size_bytes": stat.st_size,
            "md5": hashlib.md5(data).hexdigest(),
        })
    return catalog

evidence_catalog = catalog_evidence(evidence_dir)
for item in evidence_catalog:
    print(item)

def test_experiment17():
    assert os.path.isdir(evidence_dir), "Evidence directory should exist"
    assert len(evidence_catalog) == len(sample_evidence), "All evidence files should be catalogued"
    filenames = [e["filename"] for e in evidence_catalog]
    for expected in sample_evidence:
        assert expected in filenames, f"{expected} missing from catalog"
    for entry in evidence_catalog:
        assert entry["size_bytes"] > 0
        assert len(entry["md5"]) == 32
    print("Experiment 17: All test cases passed.")

test_experiment17()

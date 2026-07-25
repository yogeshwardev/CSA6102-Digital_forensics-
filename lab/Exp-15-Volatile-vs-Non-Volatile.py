import os
import psutil

evidence_dir = "digital_evidence"
# Ensure the directory exists from the previous experiment, or create it minimally for this test
os.makedirs(evidence_dir, exist_ok=True)
sample_evidence = {
    "email_log.txt": "From: attacker@mail.com\nTo: victim@mail.com\nSubject: Invoice\nPlease pay immediately.",
    "browser_history.txt": "http://malicious-site.com/login\nhttp://bank.com/transfer",
    "chat_message.txt": "Hey, did you send the file?",
    "system_log.txt": "2026-07-24 10:15:32 - USB device connected: E:\\",
}

# Ensure the files exist so the test passes
for filename, content in sample_evidence.items():
    with open(os.path.join(evidence_dir, filename), "w") as f:
        f.write(content)

def capture_volatile_evidence():
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    return {
        "running_process_count": len(processes),
        "sample_processes": processes[:5],
    }

def capture_nonvolatile_evidence(folder):
    files = sorted(os.listdir(folder))
    return {"disk_files": files, "file_count": len(files)}

volatile_snapshot = capture_volatile_evidence()
nonvolatile_snapshot = capture_nonvolatile_evidence(evidence_dir)

print("Volatile evidence -> running processes:", volatile_snapshot["running_process_count"])
print("Non-volatile evidence -> disk files:", nonvolatile_snapshot)

def test_experiment15():
    assert volatile_snapshot["running_process_count"] > 0, "There should be at least one running process"
    assert isinstance(volatile_snapshot["sample_processes"], list)
    assert nonvolatile_snapshot["file_count"] == len(sample_evidence)
    snapshot2 = capture_nonvolatile_evidence(evidence_dir)
    assert snapshot2 == nonvolatile_snapshot, "Non-volatile evidence must remain unchanged between reads"
    print("Experiment 15: All test cases passed.")

test_experiment15()

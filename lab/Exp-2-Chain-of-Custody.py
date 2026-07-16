import hashlib, datetime

def sha256_of(filename):
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# Step 1: Investigator seizes evidence and hashes it immediately
with open("evidence.txt", "w") as f:
    f.write("Suspect chat log: meeting at 10pm, bring the drive.")

seizure_hash = sha256_of("evidence.txt")
custody_log = []
custody_log.append(f"{datetime.datetime.now()} - SEIZED by Officer A - hash={seizure_hash}")

# Step 2: Evidence is later handed to a forensic analyst; verify integrity
handoff_hash = sha256_of("evidence.txt")

if handoff_hash == seizure_hash:
    custody_log.append(f"{datetime.datetime.now()} - RECEIVED by Analyst B - integrity VERIFIED")
else:
    custody_log.append(f"{datetime.datetime.now()} - RECEIVED by Analyst B - integrity FAILED (tampered!)")

print("=== Chain of Custody Log ===")
for entry in custody_log:
    print(entry)

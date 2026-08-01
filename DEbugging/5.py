import hashlib

def compute_hash(filepath):
    hasher = hashlib.sha256()

    with open(filepath, 'rb') as f:
        content = f.read()

    hasher.update(content)

    return hasher.hexdigest()

def verify_integrity(filepath):
    hash_at_collection = compute_hash(filepath)
    hash_before_analysis = compute_hash(filepath)

    if hash_at_collection == hash_before_analysis:
        print("Match: Evidence integrity verified")
    else:
        print("Mismatch: Evidence may be compromised")

verify_integrity("evidence_image.dd")
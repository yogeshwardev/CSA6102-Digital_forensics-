import hashlib

def compute_hashes(data: bytes):
    return {
        "MD5": hashlib.md5(data).hexdigest(),
        "SHA1": hashlib.sha1(data).hexdigest(),
        "SHA256": hashlib.sha256(data).hexdigest(),
    }

original_data = b"hello"
tampered_data = b"Hello"

hashes_original = compute_hashes(original_data)
hashes_tampered = compute_hashes(tampered_data)
hashes_original_repeat = compute_hashes(original_data)

print("hello ->", hashes_original)
print("Hello ->", hashes_tampered)

def test_experiment23():
    assert hashes_original == hashes_original_repeat, "Same input must always produce the same hash"
    assert hashes_original["MD5"] != hashes_tampered["MD5"], "A single-character change must alter the MD5 hash"
    assert hashes_original["SHA256"] != hashes_tampered["SHA256"], "A single-character change must alter the SHA-256 hash"
    print("Experiment 23: All test cases passed.")

test_experiment23()

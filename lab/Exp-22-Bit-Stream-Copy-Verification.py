import os
import hashlib

original_path = "original_evidence.bin"
with open(original_path, "wb") as f:
    f.write(os.urandom(1024)) # simulate a small storage device

def bit_stream_copy(src_path, dst_path):
    with open(src_path, "rb") as src, open(dst_path, "wb") as dst:
        dst.write(src.read())

copy_path = "bitstream_copy.bin"
bit_stream_copy(original_path, copy_path)

def sha256_of_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

original_hash = sha256_of_file(original_path)
copy_hash = sha256_of_file(copy_path)

print("Original hash:", original_hash)
print("Copy hash: ", copy_hash)

def test_experiment22():
    assert os.path.getsize(original_path) == os.path.getsize(copy_path), "Bit stream copy must match original size exactly"
    assert original_hash == copy_hash, "Hashes must match, proving the copy is forensically identical"
    print("Experiment 22: All test cases passed.")

test_experiment22()

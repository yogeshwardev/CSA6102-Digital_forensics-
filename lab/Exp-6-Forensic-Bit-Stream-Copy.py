import hashlib

def sha256_of(filename):
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# Create a sample "disk" file (simulating a small storage device)
with open("original_disk.img", "wb") as f:
    f.write(b"HEADER" + bytes(range(256)) * 4 + b"FOOTER")

# Step 1: Create a bit-for-bit forensic copy (bit-stream image)
with open("original_disk.img", "rb") as src, open("forensic_copy.img", "wb") as dst:
    dst.write(src.read())

# Step 2: Verify the copy is identical using hashing
original_hash = sha256_of("original_disk.img")
copy_hash = sha256_of("forensic_copy.img")

print("Original image hash:", original_hash)
print("Forensic copy hash :", copy_hash)
print("Match:", "VERIFIED - exact bit-stream copy" if original_hash == copy_hash else "MISMATCH - copy corrupted")

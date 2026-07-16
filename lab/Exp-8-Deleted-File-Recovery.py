import os

# Step 1: Create a file, then "delete" it (simulating accidental/malicious deletion)
with open("secret_note.txt", "w") as f:
    f.write("MEETING_POINT: warehouse 7, 11pm")

with open("secret_note.txt", "rb") as f:
    original_bytes = f.read()

os.remove("secret_note.txt")

print("File 'secret_note.txt' deleted.")
print("Exists on disk now?", os.path.exists("secret_note.txt"))

# Step 2: Simulate raw disk scanning - in real forensics, tools like Autopsy
# scan unallocated space for byte patterns. Here we search a "disk buffer"
# (which still holds the bytes) for the recoverable content.
disk_buffer = original_bytes + b"\x00" * 50 # unallocated space padding
marker = b"MEETING_POINT"
index = disk_buffer.find(marker)

if index != -1:
    recovered = disk_buffer[index:].split(b"\x00")[0]
    with open("recovered_note.txt", "wb") as f:
        f.write(recovered)
    print("Recovered content:", recovered.decode())
else:
    print("No recoverable data found.")

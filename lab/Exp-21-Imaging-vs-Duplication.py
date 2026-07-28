raw_disk_full = b"FILE1DATA" + b"\x00" * 15 + b"DELETED_FILE_DATA" + b"\x00" * 15 + b"FREE_SPACE_00000"

def create_forensic_image(raw_bytes):
    return bytes(raw_bytes) # bit-for-bit: files + deleted data + free space

def create_duplication(raw_bytes, active_regions):
    return b"".join(raw_bytes[start:end] for start, end in active_regions)

active_regions = [(0, 9)] # only the live "FILE1DATA" region
forensic_image = create_forensic_image(raw_disk_full)
duplication_copy = create_duplication(raw_disk_full, active_regions)

print("Forensic image size:", len(forensic_image))
print("Duplication size:", len(duplication_copy))

def test_experiment21():
    assert len(forensic_image) == len(raw_disk_full), "Imaging must capture the full storage device size"
    assert b"DELETED_FILE_DATA" in forensic_image, "Imaging must include deleted data"
    assert b"DELETED_FILE_DATA" not in duplication_copy, "Duplication must exclude deleted data"
    assert len(duplication_copy) < len(forensic_image), "Duplication should be smaller than a full image"
    print("Experiment 21: All test cases passed.")

test_experiment21()

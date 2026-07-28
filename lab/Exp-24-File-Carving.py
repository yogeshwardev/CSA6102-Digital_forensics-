import os

def make_fake_jpeg(payload: bytes):
    return b"\xff\xd8\xff" + payload + b"\xff\xd9"

jpeg1 = make_fake_jpeg(b"PHOTO_OF_SUSPECT_CAR")
jpeg2 = make_fake_jpeg(b"CCTV_FRAME_CAPTURE")
raw_disk_blob = os.urandom(30) + jpeg1 + os.urandom(40) + jpeg2 + os.urandom(20)

def carve_jpegs(blob: bytes):
    recovered = []
    start_marker, end_marker = b"\xff\xd8\xff", b"\xff\xd9"
    pos = 0
    while True:
        start = blob.find(start_marker, pos)
        if start == -1:
            break
        end = blob.find(end_marker, start)
        if end == -1:
            break
        end += len(end_marker)
        recovered.append(blob[start:end])
        pos = end
    return recovered

recovered_files = carve_jpegs(raw_disk_blob)
print("Recovered", len(recovered_files), "file(s) via carving")

def test_experiment24():
    assert len(recovered_files) == 2, "File carving should recover exactly 2 embedded JPEGs"
    assert recovered_files[0] == jpeg1, "First recovered file must exactly match the original embedded JPEG"
    assert recovered_files[1] == jpeg2, "Second recovered file must exactly match the original embedded JPEG"
    print("Experiment 24: All test cases passed.")

test_experiment24()

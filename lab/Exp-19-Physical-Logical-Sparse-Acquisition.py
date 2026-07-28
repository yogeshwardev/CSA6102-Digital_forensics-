import os

os.makedirs("acquisition_demo/source", exist_ok=True)
source = "acquisition_demo/source"

with open(os.path.join(source, "report.docx"), "w") as f:
    f.write("Confidential quarterly report.")
with open(os.path.join(source, "photo.jpg"), "w") as f:
    f.write("FAKEJPEGDATA")

raw_disk = b"REPORTDOCX_CONTENT" + b"\x00" * 20 + b"DELETED_INVOICE_DATA" + b"\x00" * 10

def physical_acquisition(raw_bytes):
    return bytes(raw_bytes) # every bit: used + unused + deleted

def logical_acquisition(folder):
    return {f: open(os.path.join(folder, f), "rb").read() for f in os.listdir(folder)}

def sparse_acquisition(folder, targets):
    return {f: open(os.path.join(folder, f), "rb").read() for f in targets if f in os.listdir(folder)}

physical_image = physical_acquisition(raw_disk)
logical_image = logical_acquisition(source)
sparse_image = sparse_acquisition(source, ["report.docx"])

print("Physical image size:", len(physical_image), "bytes")
print("Logical image files:", list(logical_image.keys()))
print("Sparse image files:", list(sparse_image.keys()))

def test_experiment19():
    assert physical_image == raw_disk, "Physical acquisition must be an exact byte-for-byte copy"
    assert b"DELETED_INVOICE_DATA" in physical_image, "Physical acquisition must include deleted/unused regions"
    assert set(logical_image.keys()) == {"report.docx", "photo.jpg"}, "Logical acquisition should copy all visible files"
    assert set(sparse_image.keys()) == {"report.docx"}, "Sparse acquisition should copy only the targeted file"
    print("Experiment 19: All test cases passed.")

test_experiment19()

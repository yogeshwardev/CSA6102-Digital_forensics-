SIGNATURES = {
    b"\xFF\xD8\xFF": "JPEG image",
    b"\x89PNG": "PNG image",
    b"%PDF": "PDF document",
    b"PK\x03\x04": "ZIP archive (or .docx/.xlsx)",
}

def identify_file(path):
    with open(path, "rb") as f:
        header = f.read(8)
        for sig, filetype in SIGNATURES.items():
            if header.startswith(sig):
                return filetype
        return "Unknown file type"

# Create sample files with fake/renamed extensions to test signature detection
with open("photo.txt", "wb") as f: # renamed JPEG
    f.write(b"\xFF\xD8\xFF\xE0" + b"\x00" * 20)

with open("document.dat", "wb") as f: # renamed PDF
    f.write(b"%PDF-1.4" + b"\x00" * 20)

for filename in ["photo.txt", "document.dat"]:
    print(f"{filename:15s} -> Actual type: {identify_file(filename)}")

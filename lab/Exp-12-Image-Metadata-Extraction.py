from PIL import Image
from PIL.ExifTags import TAGS
# Install once: pip install Pillow

def create_sample_image(path):
    # Creates a small test image (a real photo would already have EXIF data)
    img = Image.new("RGB", (100, 100), color="blue")
    img.save(path)

def show_metadata(path):
    img = Image.open(path)
    print("File:", path)
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)
    
    exif_data = img._getexif() if hasattr(img, "_getexif") else None
    
    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f" {tag}: {value}")
    else:
        print(" No EXIF metadata found (this sample image has none).")
        print(" Real photos from phones/cameras typically contain GPS,")
        print(" device model, and timestamp data - valuable forensic evidence.")

create_sample_image("sample.jpg")
show_metadata("sample.jpg")

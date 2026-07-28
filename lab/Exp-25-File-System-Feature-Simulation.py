class FATFileEntry:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        # FAT intentionally has no permissions or journal attribute

class NTFSFileEntry:
    def __init__(self, name, size, permissions="rw-r--r--"):
        self.name = name
        self.size = size
        self.permissions = permissions
        self.journal_entry = f"WRITE {name} {size} bytes"

class EXTFileEntry:
    def __init__(self, name, size, permissions="rw-r--r--"):
        self.name = name
        self.size = size
        self.permissions = permissions
        self.journal_entry = f"WRITE {name} {size} bytes"

fat_file = FATFileEntry("data.txt", 1024)
ntfs_file = NTFSFileEntry("data.txt", 1024)
ext_file = EXTFileEntry("data.txt", 1024)

print("FAT has permissions attribute:", hasattr(fat_file, "permissions"))
print("NTFS has permissions attribute:", hasattr(ntfs_file, "permissions"))
print("EXT has permissions attribute:", hasattr(ext_file, "permissions"))

def test_experiment25():
    assert not hasattr(fat_file, "permissions"), "FAT should not support file permissions"
    assert not hasattr(fat_file, "journal_entry"), "FAT should not support journaling"
    assert hasattr(ntfs_file, "permissions") and hasattr(ntfs_file, "journal_entry"), "NTFS should support permissions and journaling"
    assert hasattr(ext_file, "permissions") and hasattr(ext_file, "journal_entry"), "EXT should support permissions and journaling"
    print("Experiment 25: All test cases passed.")

test_experiment25()

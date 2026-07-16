import os, shutil, time

# Create an "original" piece of evidence
with open("evidence_original.txt", "w") as f:
    f.write("Case File #001 - Suspect device log")

orig_stat = os.stat("evidence_original.txt")
print("Original file - created (ctime):", time.ctime(orig_stat.st_ctime))
print("Original file - modified (mtime):", time.ctime(orig_stat.st_mtime))

# Simulate an investigator copying the file to a workstation
time.sleep(1)
shutil.copy2("evidence_original.txt", "evidence_copy.txt")

copy_stat = os.stat("evidence_copy.txt")
print("\nCopied file - created (ctime):", time.ctime(copy_stat.st_ctime))
print("Copied file - modified (mtime):", time.ctime(copy_stat.st_mtime))

print("\nLocard's Exchange Principle: the copy operation itself created a new")
print("ctime on the destination file - every interaction leaves a trace.")

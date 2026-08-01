volatile_sources = [
    'RAM',
    'Cache',
    'Running Processes',
    'Network Connections',
    'Swap File'
]

def classify(source):
    if source in volatile_sources:
        return "Volatile"
    else:
        return "Non-Volatile"

evidence_sources = [
    'RAM',
    'Hard Disk',
    'Cache',
    'Registry Files'
]

for src in evidence_sources:
    print(src, ":", classify(src))
import math
from collections import Counter

def shannon_entropy(s):
    if not s:
        return 0.0
    counts = Counter(s)
    length = len(s)
    return -sum((c / length) * math.log2(c / length) for c in counts.values())

def detect_dns_tunneling(queries, length_threshold=20, entropy_threshold=3.5):
    """queries: list of fully-qualified domain name strings.
    Flags queries whose leftmost label is long AND high-entropy."""
    flagged = []
    for q in queries:
        label = q.split(".")[0]
        entropy = shannon_entropy(label)
        if len(label) >= length_threshold and entropy >= entropy_threshold:
            flagged.append({"query": q, "label_length": len(label), "entropy": round(entropy, 2)})
    return flagged

def test_experiment34():
    queries = [
        "www.google.com",
        "mail.office365.com",
        "a8f3k2j9x1p7q4z6w0n5r2t8y3.exfil-domain.com",
        "vpn.corporate-network.com",
        "9c2e7b1a4f8d3c6e0a5b9d2f7c1e4a8b3d6f9c2e5a8b1d4f.tunnel.example.net",
    ]
    flagged = detect_dns_tunneling(queries)
    flagged_domains = [f["query"] for f in flagged]
    assert "www.google.com" not in flagged_domains
    assert "mail.office365.com" not in flagged_domains
    assert "vpn.corporate-network.com" not in flagged_domains
    assert "a8f3k2j9x1p7q4z6w0n5r2t8y3.exfil-domain.com" in flagged_domains
    assert "9c2e7b1a4f8d3c6e0a5b9d2f7c1e4a8b3d6f9c2e5a8b1d4f.tunnel.example.net" in flagged_domains
    assert len(flagged) == 2
    print("Experiment 34: All test cases passed.")

test_experiment34()

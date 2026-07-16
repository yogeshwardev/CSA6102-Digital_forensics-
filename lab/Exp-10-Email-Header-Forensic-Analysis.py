raw_header = """Delivered-To: victim@example.com
Received: from mail-relay-99.suspicious-host.ru (unknown [45.33.32.156])
by mx.example.com; Tue, 08 Jul 2026 09:15:00 +0000
From: \"Bank Support\" <support@paypal-secure-verify.com>
Reply-To: attacker@totallynotscam.net
Subject: Urgent: Verify your account
"""

def analyze_header(header_text):
    findings = []
    for line in header_text.splitlines():
        if line.startswith("Received:") and "suspicious" in line.lower():
            findings.append(f"Suspicious relay server found: {line.strip()}")
        if line.startswith("Reply-To:"):
            findings.append(f"Reply-To differs from sender - possible spoofing: {line.strip()}")
        if line.startswith("From:") and "-secure-verify" in line:
            findings.append(f"Sender domain uses suspicious naming: {line.strip()}")
    return findings

print("Email Header Forensic Analysis")
for finding in analyze_header(raw_header):
    print(" -", finding)

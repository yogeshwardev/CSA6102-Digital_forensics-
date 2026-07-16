import datetime

def generate_forensic_report(case_id, findings, investigator):
    lines = []
    lines.append("DIGITAL FORENSIC INVESTIGATION REPORT")
    lines.append(f"Case ID: {case_id}")
    lines.append(f"Investigator: {investigator}")
    lines.append(f"Report generated: {datetime.datetime.now()}")
    lines.append("-" * 45)
    lines.append("FINDINGS:")
    for i, finding in enumerate(findings, 1):
        lines.append(f" {i}. {finding}")
    lines.append("-" * 45)
    lines.append("CONCLUSION:")
    lines.append(" Evidence indicates unauthorized access consistent with a")
    lines.append(" brute-force attack. Recommend IP block and password reset.")
    lines.append(" This report is suitable for legal review and expert testimony.")
    return "\n".join(lines)

findings = [
    "203.0.113.99 attempted 5 failed logins within 20 seconds (log file evidence).",
    "SHA-256 hash of evidence file verified unchanged throughout custody.",
    "Email header traced to a spoofed domain via suspicious relay server.",
]

report = generate_forensic_report("CASE-2026-014", findings, "Analyst B")
print(report)

with open("forensic_report.txt", "w") as f:
    f.write(report)

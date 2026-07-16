import datetime

def investigation_report(case_id, evidence_list):
    stages = {
        "Identification": f"Incident reported for case {case_id}. Devices/logs identified for review.",
        "Collection": f"{len(evidence_list)} item(s) collected: {', '.join(evidence_list)}",
        "Preservation": "All items hashed (SHA-256) and stored in a write-protected evidence folder.",
        "Analysis": "Log files and file metadata examined for indicators of compromise.",
        "Reporting": "Findings compiled into a structured forensic report for legal review.",
    }
    
    print(f"=== Investigation Lifecycle: Case {case_id} ===")
    print(f"Generated: {datetime.datetime.now()}\n")
    
    for stage, detail in stages.items():
        print(f"[{stage}]")
        print(f" {detail}\n")

investigation_report("CASE-2026-014", ["laptop_disk_image.dd", "router_traffic.pcap", "email_headers.txt"])

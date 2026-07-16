import re

def check_email(sender, subject, body):
    flags = []
    if re.search(r"(urgent|verify your account|suspended|click here)", body, re.IGNORECASE):
        flags.append("Urgency/pressure language detected")
        
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", body):
        flags.append("Raw IP address link found in body")
        
    domain = sender.split("@")[-1]
    if any(k in domain.lower() for k in ["secure","verify","update"]) and "@gmail" not in sender:
        flags.append("Suspicious sender domain naming pattern")
        
    return flags

emails = [
    ("support@paypal.com", "Your monthly statement", "Please find your statement attached."),
    ("alert@paypal-secure-verify.com", "URGENT: Verify your account", "Click here: http://192.168.10.5/login"),
]

for sender, subject, body in emails:
    issues = check_email(sender, subject, body)
    verdict = "PHISHING SUSPECTED" if issues else "Looks legitimate"
    print(f"\nFrom: {sender}\nSubject: {subject}\nVerdict: {verdict}")
    for i in issues:
        print(" -", i)

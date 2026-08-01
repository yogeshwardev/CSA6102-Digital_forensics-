def classify_incident(description):
    categories = {
        'Phishing': ['fake email', 'login link', 'credential'],
        'Ransomware': ['encrypted files', 'ransom note', 'bitcoin'],
        'Identity Theft': ['stolen identity', 'aadhaar', 'pan card']
    }

    description = description.lower()

    for category, keywords in categories.items():
        for word in keywords:
            if word in description:
                return category

    return "Unclassified"

result = classify_incident(
    "Victim received a fake email with a login link")

print(result)
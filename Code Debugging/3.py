import re

def is_suspicious(url):
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    suspicious_words = ('verify', 'update', 'secure', 'login')

    if re.search(ip_pattern, url):
        return True

    for word in suspicious_words:
        if word in url:
            return True

    return False

urls = [
    'http://192.168.1.10/verify-account',
    'https://mybank.com/login'
]

for u in urls:
    print(u, "->", is_suspicious(u))
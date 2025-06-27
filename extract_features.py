import re
from urllib.parse import urlparse

def has_ip(url):
    return 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

def has_at_symbol(url):
    return 1 if '@' in url else 0

def url_length(url):
    return len(url)

def has_https(url):
    return 1 if url.startswith("https") else 0

def extract_features(url):
    return [
        has_ip(url),
        has_at_symbol(url),
        url_length(url),
        has_https(url)
    ]

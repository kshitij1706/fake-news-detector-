import tldextract

def check_source(url):
    domain = tldextract.extract(url).registered_domain
    known_fake = ["abcnews.com.co", "react365.com"]
    if domain in known_fake:
        return 0.2
    return 0.8

import uuid
database = {}

def shorten_url(long_url):
    short_url = str(uuid.uuid4())[:8]
    database[short_url] = long_url
    return short_url

def redirect_url(short_url):
    return database.get(short_url)

# Example usage
long_url = "https://example.com/some/long/url"
short_url = shorten_url(long_url)
print("Short URl:", short_url)
print("Redirect URL:", redirect_url(short_url))

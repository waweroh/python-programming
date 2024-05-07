import requests

URL = "https://hojaleaks.com/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

if __name__ == "__main__":
    print(scrape(URL))
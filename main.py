import requests, urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from config import signatures


def fetch_article(URL):
    try:
        html = requests.get(URL).content
    except requests.exceptions.MissingSchema() as e:
        print("Error please specify url with scheme")

    # Feed html into parser2 and extract hostname
    soup = BeautifulSoup(html, "html.parser")
    hostname = urlparse(URL).hostname

    # Parse html by signatures from config.py. Use table of div global tag
    article_body = soup.find("table", signatures[hostname])
    if not article_body:
        article_body = soup.find("div", signatures[hostname])

    return article_body



# ARTICLE_URL = 'https://habr.com/ru/post/592071/'
ARTICLE_URL = 'https://www.opennet.ru/opennews/art.shtml?num=56270'
# ARTICLE_URL = 'https://losst.ru/ustanovka-programm-v-astra-linux'

article_body = fetch_article(ARTICLE_URL)
print(article_body)

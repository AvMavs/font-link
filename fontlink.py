import requests
from bs4 import BeautifulSoup

def get_font_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    fonts_link = []
    for tag in soup.find_all(["link"]):
        if 'href' in tag.attrs and (tag['href'].endswith('.woff') or tag['href'].endswith('.woff2') or tag['href'].endswith('.ttf') or tag['href'].endswith('.otf')):
            fonts_link.append(tag['href'])
    return fonts_link

url = "https://yourlinkhere"
font_links = get_font_links(url)
print(font_links)

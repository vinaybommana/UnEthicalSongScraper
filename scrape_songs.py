import os
import requests
from bs4 import BeautifulSoup


def get_songs_links(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    refs = [i.get('href') for i in links]
    refs = refs[5:]
    return refs


def get_songs(links, l):
    for link in links:
        os.system("curl {}{}' --output {}".format(l, link, link))


def main():
    link = "http://bitashop.org/Download/Bita/Music/Full%20Album/Taylor%20Swift%20-%20Full%20Album/Taylor%20Swift%20-%20(2006)%20Taylor%20Swift/"
    print(get_songs(get_songs_links(link), link))


if __name__ == "__main__":
    main()

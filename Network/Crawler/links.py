import sys

import requests
from bs4 import BeautifulSoup

files = []


def get_links(url):
    print url
    r = requests.get(url)
    contents = r.content

    soup = BeautifulSoup(contents, "lxml")
    links = []
    for link in soup.findAll('a'):
        try:
            links.append(link['href'])
            print link['href']
            if link['href'].endswith("rar"):
                files.append(url + link['href'])
        except KeyError:
            pass
    return links


if __name__ == "__main__":
    # url = sys.argv[1]
    url = "http://server4.xytune.ir/server4/"
    urls2 = get_links(url)
    urls4 = []
    for u in urls2:
        urls3 = get_links(url + u)
        print urls3
    # for u in urls3:
    #     urls4.append(get_links(url + "/" + u))
    # print files
    sys.exit()

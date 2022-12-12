import contextlib
import requests
from bs4 import BeautifulSoup

LINK = "https://boards.greenhouse.io/wargamingen"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  Safari/537.36',
    'Referer': 'https://boards.greenhouse.io/',
    'Connection': 'keep-alive',
}

def get_info(link,client):
    link = f"https://boards.greenhouse.io{link}"
    html = client.get(link, headers= HEADERS)
    page = BeautifulSoup(html.text, 'html.parser')
    header = page.find('div', id='header')
    content = page.find('div', id='content')
    for i, li in enumerate(content.find_all('ul')):
        name = content.find_all('h3')
        print(name[i].get_text())
        for _  in li.find_all('li'):
            print("●" , _.get_text().strip())
        


def get_vacancies():
    client = requests.session()
    html = client.get(LINK, headers= HEADERS)
    content = BeautifulSoup(html.text, 'html.parser')
    d = []
    for i, link in enumerate(content.find_all('div')[:-2], start=1):
        l2 = link.find('a')
        with contextlib.suppress(Exception):
            get_info(l2['href'], client)
            # d.append(
            #     {
            #         "id":i,
            #         "Position": l2.get_text(),
            #         "Link": "https://boards.greenhouse.io" + l2['href'],
            #         "Location": link.find('span').get_text()
            #     })


get_info('/wargamingen/jobs/4617814', requests.session())

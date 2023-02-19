import requests
#
# 'https://xkcd.com/353/'
#
# r = requests.get('https://xkcd.com/353/', timeout=3)
# print(r)
#
# pic = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=4)
# with open('comic.png', 'wb') as file:
#     file.write(pic.content)

from bs4 import BeautifulSoup as BS

url = 'https://www.gammatest.net/course/python/'
full_page = requests.get(url, timeout=5)

soup = BS(full_page.content, 'html.parser')
match = soup.find_all('div', class_='col-md-4 col-sm-12')
for div in match:
    links = div.find_all('a')
    for link in links:
        print(link['href'])
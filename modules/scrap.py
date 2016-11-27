import urllib.request
from bs4 import BeautifulSoup
import json


res = urllib.request.urlopen('http://www.imdb.com/list/ls055592025/')
soup = BeautifulSoup(res, "html.parser")

movList = {}
i = 0
links = []
titles = []

loadLate = 'loadlate zero-z-index'

for div in soup.findAll('div', {'class': 'info'}):
    for b in div.findAll('b'):
        for a in b.findAll('a'):
            titles.append(a.text)
            links.append(a['href'])
            movList[str(a.text)] = ''

with open('movList.json', 'w') as fp:
    json.dump(movList,fp)

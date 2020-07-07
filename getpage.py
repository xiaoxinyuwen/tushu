
import requests
from bs4 import BeautifulSoup
def getPage():
    list = []
    url = 'https://www.winxuan.com/catalog_book.html'
    res = requests.get(url).text
    soup = BeautifulSoup(res,'html.parser')
    div = soup.find_all('div',class_='all_cate')[0]
    for dd in div.find_all('dd'):
        for aa in dd.find_all('a'):
            tmp = []
            a = aa['href']
            b = aa.text
            res = requests.get(a).text
            soup = BeautifulSoup(res,'html.parser')
            div = soup.find_all('div',class_='sg-commentpage')
            tmp = [a,b]
            list.append(tmp)
    return list

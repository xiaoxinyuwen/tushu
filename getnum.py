import requests
from bs4 import BeautifulSoup
url = 'https://list.winxuan.com/1101'
from getpage import getPage
list = getPage()
def getNum():
    for i in range(len(list)):
        url = list[i][0]
        res = requests.get(url).text
        soup = BeautifulSoup(res,'html.parser')
        try:
            div = soup.find_all('div',class_='sg-commentpage')[0]
        except:
            print('丢失页面')
        num = int(div.find_all('a')[-2].text)
        print(num)
getNum()


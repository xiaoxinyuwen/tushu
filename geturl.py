from getpage import getPage
url = 'https://list.winxuan.com/1101?size=20&page=2'
list = getPage()

def getUrl(list):
    urls = []
    for i in list:
        for j in range(1,51):
            url = i[0] + '?size=20&page=' + str(j)
            urls.append(url)
    return urls


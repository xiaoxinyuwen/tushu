
from getInfo import getInfo
from wInExcel import openxl
from geturl import getUrl
from getpage import getPage
list = getPage()
urls = getUrl(list)
l = []
for url in urls:
    print(url)
    list = getInfo(url)
    l.extend(list)
openxl(l)
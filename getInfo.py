import requests
from bs4 import BeautifulSoup
headers = {
    "Accept":"application/json",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection":"keep-alive",
    "Cookie":"ll='118281';bid=Etv6UnhrxhQ;__utmz=30149280.1592379663.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;__utma=30149280.667647424.1592379663.1592379663.1594030525.2;gr_user_id=bbf32300-49db-44f2-8d7e-c54768b190fc;_vwo_uuid_v2=D47ADF60A5EE16EBE030747447B76F2F5|6ea9069dc78718e6f4520da5d424c9ee;_ga=GA1.3.667647424.1592379663; _gid=GA1.3.1511970949.1594030549;__gads=ID=c43c6fd8f82bdbf3:T=1594030550:S=ALNI_MaH7VSS5bV7hgRTCy0LFL3232fuMA;_pk_ref.100001.a7dd=%5B%22%22%2C%22%22%2C1594089149%2C%22https%3A%2F%2Fbook.douban.com%2F%22%5D;_pk_id.100001.a7dd=829b893526426ba5.1594030549.3.1594089149.1594085033.;_pk_ses.100001.a7dd=*;_gat=1",
    "Host":"read.douban.com",
    "Referer":"https://read.douban.com/category?kind=100",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
'''
<div class="cell cell-m-book-top-pop"><div class="img"><a href="https://item.winxuan.com/1200690487" target="_blank" title="儒林外史 ">
<img alt="儒林外史 " src="//img0.winxuancdn.com/0552/1200690552_11_1.jpg?1502601156323"/></a></div><div class="name">
<a href="https://item.winxuan.com/1200690487" target="_blank" title="儒林外史 ">儒林外史 </a></div><div class="price">
<span class="price-n">￥13.00</span><span class="price-o">￥13.00</span></div><div class="active">
<a bind="addToCart" class="btn-shoppingcart" data-id="1200690487" href="javascript:;"></a></div><div class="attr">
<div class="author">(清)<a href="http://search.winxuan.com/search?author=%E5%90%B4%E6%95%AC%E6%A2%93" style="color:#1D66B2">吴敬梓</a>  
 </div><div class="evaluate"><b class="star5"></b></div><div class="publisher"><span>出 版 社 :</span> 
 <a href="https://search.winxuan.com/search?manufacturer=%e5%8d%8e%e5%a4%8f%e5%87%ba%e7%89%88%e7%a4%be+">华夏出版社 </a>
 </div><div class="publishingtime"><span>出版时间 ：</span>2013年04月</div></div></div>
'''
def getInfo(url):
    list = []
    try:
        res = requests.get(url).text
    except:
        print('没有这个网页，请忽略...')
    soup = BeautifulSoup(res,'html.parser')
    try:
        for info in soup.find_all('div',class_='cell cell-m-book-top-pop'):
            tmp = []
            #书名
            try:
                bookname = info.find('div',class_='img').a['title']
            except:
                print('书名为空')
                bookname = '缺失'
            tmp.append(bookname)
            #作者
            try:
                name = info.find('div',class_='author').a.text
            except:
                print('作者名字为空')
                name = '缺失'
            tmp.append(name)
            #价格
            try:
                price = info.find('span',class_='price-n').text
            except:
                print('价格缺失')
                price = '缺失'
            tmp.append(price)
            #出版社
            try:
                publisher = info.find('div',class_='publisher').a.text
            except:
                print('出版社缺失')
                publisher = '缺失'
            tmp.append(publisher)
            #出版时间
            try:
                ptime = info.find('div',class_='publishingtime').text
            except:
                print('出版时间缺失')
                ptime = '缺失'
            tmp.append(ptime)
            list.append(tmp)
    except:
        print('find_all失败...')
    return list



# url = 'https://list.winxuan.com/1301?size=20&page=1'
# getInfo(url)
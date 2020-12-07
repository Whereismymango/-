import os,requests,bs4,threading
url = 'https://pawgsonly.com/sites/ass-parade/' 
res = requests.get(url)
res.encoding = 'utf-8'
res.raise_for_status
print(res.status_code)
soup = bs4.BeautifulSoup(res.text,'html.parser')
elems = soup.select('.item  a')
#print(elems)
print(len(elems))
for i in elems:
    newurl = i.get('href')    
    newres = requests.get(newurl)
    newres.encoding = 'utf-8'
    newres.raise_for_status
    #print(i.get_text() + '   的请求码为：' + str(newres.status_code))
    newsoup = bs4.BeautifulSoup(newres.text,'html.parser')
    newelems = newsoup.select('div video')
    #print(i.get_text() + '项下的图片有：' )
    for i in newelems:
        print(i.get('src'))
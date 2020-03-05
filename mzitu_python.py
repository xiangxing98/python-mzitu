import requests
import os
import re
import urllib
from bs4 import BeautifulSoup
####################
orig_url='http://www.mzitu.com/'
folder = 'F:/我的文件/about python/mzitu_python/'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
'Referer':'http://www.mzitu.com/'
    }
####################
if not os.path.exists(folder):
    os.makedirs(folder)

resp = urllib.request.urlopen(orig_url)
html = resp.read()
bs=BeautifulSoup(html,'html.parser')
li=bs.find('ul',id='pins').find_all('a')##获取标签href值
#print(li)
url_list =[]
flag=0
for i in li:
    flag+=1
    if flag%2==0:
        continue
    else:
        url_list.append(i['href'])##将首页各封图网址保存在列表中
print(url_list)
for i in url_list:
    request = urllib.request.urlopen(i)
    html=request.read()
    bs=BeautifulSoup(html,'html.parser')
    page = bs.find('div',class_='pagenavi').find_all('a')[4].find('span')
    title=bs.find('h2',class_='main-title').text
    print(title)
    folder_pic = folder+title+'/'
    if not os.path.exists(folder_pic):
        os.makedirs(folder_pic)
    
    pages=int(page.text)##获取图片总数
    pages+=1
    #print(pages)
    pic_img = bs.find('div',class_='main-image').find('img')['src']
    pic_img=pic_img[0:33]
    print(pic_img)
    ############################
    for j in range(1,pages):
        if j<10:
            request = requests.get(pic_img+'0'+str(j)+'.jpg',headers=headers)
        else:
            request = requests.get(pic_img+str(j)+'.jpg',headers=headers)
        #print(pic_img+str(j)+'.jpg')
        print(str(i)+'套图的'+str(j)+'.jpg爬取完成！')
        f = open(folder_pic+str(j)+'.png','wb')
        f.write(request.content)
        f.close()
##    print('#################################################################')

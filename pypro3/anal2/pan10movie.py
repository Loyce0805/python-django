'''
Created on 2022. 4. 20.

'''
# 네이버 제공 영화 랭킹 읽기
from bs4 import BeautifulSoup

# 방법 1: urllib.request
import urllib.request as req

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
data = req.urlopen(url)
soup = BeautifulSoup(data, 'lxml') # html.parser

# print(soup.select("div.tit3"))
# print(soup.select("div[class=tit3]"))
# print(soup.findAll("div",{'class':'tit3'}))
print(soup.find_all("div",{'class':'tit3'}))

for tag in soup.find_all("div",{'class':'tit3'}):
    print(tag.text.strip())   # strip()으로 공백 없애줌
    
print('-------------------')
# 방법 2: requests
import requests
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
data = requests.get(url).text   # data = urllib.request.urlopen(url)
soup2 = BeautifulSoup(data, 'html.parser') # 'lxml'
m_list = soup2.find_all('div', 'tit3')

# print(m_list)
count = 1
for i in m_list:
    title = i.find('a')
    print(str(count)+"위:" + title.string)
    count += 1
'''
Created on 2022. 4. 20.

'''
# 크롤링과 스크래핑의 차이
# 스크래핑 : 해당 페이지 하나만 딱 긁는건 스크래핑
# 크롤링 : 사이트를 계속 돌아다니면서 데이터를 긁는건 크롤링
# import requests
import urllib.request as req
from bs4 import BeautifulSoup

# 위키백과 사이트에서 이순신으로 검색된 자료 읽기
url = 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0'
wiki = req.urlopen(url)
# print(wiki.read())

soup = BeautifulSoup(wiki, 'html.parser')   # lxml도 가능
#print(soup)
#mw-content-text > div.mw-parser-output > p:nth-child(5)  # 우클릭 -> copy -> select copy
print(soup.select("#mw-content-text > div.mw-parser-output > p"))

#ss = soup.select("#mw-content-text > div.mw-parser-output > p > b")
ss = soup.select("#mw-content-text > div.mw-parser-output > p")
for s in ss:
    if s.string != None:
        print(s.string)
        
print('-----------------------------------')
url2 = "https://news.daum.net/society#1"
daum = req.urlopen(url2)
soup2 = BeautifulSoup(daum, 'lxml')
print(soup2.select_one("body > div.direct-link > a").string)

datas = soup2.select("div.direct-link > a")
print(datas)
for i in datas:
    href = i.attrs['href']
    ss = i.string
    print('href:%s, text:%s'%(href, ss))

print()
datas = soup2.findAll('a')
# print(datas)
for i in datas[:20]:
    href = i.attrs['href']
    ss = i.string
    print('href:%s, text:%s'%(href, ss))







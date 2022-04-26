'''
Created on 2022. 4. 19. 17:20

'''
# BeautifulSoup 객체의 find(), select() 연습
from bs4 import BeautifulSoup

html_page = """
<html>
<body>
<h1>제목 태그</h1>
<p>웹문서 읽기</p>
<p>파이썬 라이브러리 사용</p>
</body>
</html>
"""
print(html_page, type(html_page))

soup = BeautifulSoup(html_page, 'html.parser') # BeautifulSoup 객체 생성
print(soup, type(soup))

print()
h1 = soup.html.body.h1
print(h1)
print('h1:', h1.string)

p1 = soup.html.body.p
print(p1)
print('p1:', p1.text)

p2 = p1.next_sibling.next_sibling   # next_sibling을 한번만 하면 </p>가 되므로 한번 더해줌
print(p2)

print('\nfind() 사용 ---')
html_page2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹문서 읽기</p>
<p id="my" class="our">파이썬 라이브러리 사용</p>
</body>
</html>
"""
soup2 = BeautifulSoup(html_page2, 'lxml') # BeautifulSoup 객체 생성
print(soup2.p, ' ', soup2.p.string)  # 직접 최초 p tag 선택
print(soup2.find('p').string)   # find는 기본적으로 최초의 p를 찾는다.
print(soup2.find('p', id='my').string)   # id를 붙이면 id가 어쩌고인 녀석을 찾아간다.
print()
# print(soup2.find(['p', 'h1']))    # h1 tag를 땡겼다. 왜 p는 안읽지?
print(soup2.find(id='my').string)  # id만 써도 그 id를 쓰는 걸 읽어옴.
print(soup2.find(id='title').string)
print(soup2.find(class_='our').string)
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'title'}).string)

print('\nfind_all(), findAll() 사용 ---')
html_page3 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>웹문서 읽기</p>
<p id="my" class="our">파이썬 라이브러리 사용</p>
<div>
    <a href="https://www.naver.com">네이버</a>
    <a href="https://www.daum.net">다음</a>
</div>
</body>
</html>
"""
soup3 = BeautifulSoup(html_page3, 'lxml') # 'html.parser'이 lxml 대신 가능
print(soup3.find_all(['a'])) # find를 쓰면 맨 앞 1개만 가져오지만 all을 쓰면 다 가져온다.
print(soup3.find_all(['a', 'p']))
print(soup3.findAll(['a', 'p']))
print(soup3.find_all('a')) # 하나만 가져올땐 대괄호 없이 해도 a태그 전체를 가져온다.

links= soup3.find_all('a')
for i in links:
    href = i.attrs['href']
    text = i.string
    print(href, ' ', text)
    
print()
import re  # 정규표현식(레귤러익스프레션)
links2 = soup3.find_all(href = re.compile(r'^https'))   # 정규 표현식 # https로 시작하는 그런 녀석들만 find 해줘
print(links2)

print('\n셀렉터(css의 selector) ---')
html_page4 = """
<html>
<body>
<div>
    first div
</div>
<div id="hello">
    <b> 파이썬 만세</b>
    <a href="https://www.kbs.com">kbs</a>
    <a href="https://www.mbc.com">mbc</a>
    <span>
        <a href="https://www.tvn.com">tvn</a>
    </span>
</div>
<span>
    <a href="https://www.mbc.com">mbc</a>
</span>
<ul class="world">
    <li>안녕</li>
    <li>반가워</li>
</ul>
<div id="hi" class="good">
    second div
    <a href="https://www.ytn.com">ytn</a>
</div>
</body>
</html>
"""
soup4 = BeautifulSoup(html_page4, 'html.parser')   # lxml도 가능
aa = soup4.select_one("div")  # 단수 선택. 첫번째 div태그를 잡는다.
print(aa)
print('---')
bb = soup4.select_one("div#hello")   # id가 hello인 녀석을 select  #은 id .은 class
print(bb)
print('^^^')
cc = soup4.select_one("div#hello > a")  # hello 중에서 a태그 첫번째 하나만 셀렉트
print(cc)
print(cc.string)   # String인 kbs만 꺼냄

print('~~~~~~~~~~~~~~')
dd = soup4.select("div#hello > a")     # 복수 선택 (직계 자식만 추출) tvn 안나온다. 자식 요소의 a tag만 나온다.
print(dd)
ee = soup4.select("div#hello a")     # 복수 선택 (자손까지 추출) tvn까지 나온다. a tag는 전부 다나옴.
print(ee)
ff = soup4.select("ul.world > li")  # ul에서 class가 world인 녀석 #은 id .은 class
for k in ff:
    print("li : ", k.string)

print()
msg = list()   # msg = []
for k in ff:
    msg.append(k.string)

import pandas as pd
df = pd.DataFrame(msg, columns = ['자료'])
print(df)

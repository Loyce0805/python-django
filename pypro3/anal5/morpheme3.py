'''
Created on 2022. 4. 26. 형태소를 이용한 워드클라우드
'''
# 인터넷에서 특정 단어로 검색된 문서를 읽어 형태소 분석 후 명사만 추출해 워드클라우드 실행

# pip install pygame
# pip install simplejson
# pip install pytagcloud  # 이 pip가 위 2개를 필요로 함. pip는 전부 lib > sitepackage로 들어간다.

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

"""
keyword = input('검색어 입력 : ')
print(keyword)
print(quote(keyword))
"""
keyword = quote('마스크')

# 신문사 검색 기능 이용
url = "https://www.donga.com/news/search?query=" + keyword
# print(url)
source = urllib.request.urlopen(url)
soup = BeautifulSoup(source, 'lxml', from_encoding='UTF-8')
# print(soup)

msg = ""
for title in soup.find_all('p', 'tit'):
    
    title_link = title.select('a')
    # print(title_link)
    article_url = title_link[0]['href'] 
    # print(article_url) #https://www.donga.com/news/article/all/20220426/113080623/1
    try:
        source_article = urllib.request.urlopen(article_url) # 각 타이틀에 있는 기사 내용을 읽는다.
        soup = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
        contents = soup.select('div.article_txt')
        # print(contents)
        for imsi in contents:
            item = str(imsi.find_all(text=True))  # text만 가져오기. text는 절대 Text로 쓰면 안된다.
            # print(item)
            msg = msg + item
    except Exception as e:
        # print('err : ', e)
        pass  # 없는 값들은 그냥 넘기는 것

# print(msg)
from konlpy.tag import Okt
from collections import Counter # 단어 갯수 세어주는 모듈
okt = Okt()
nouns = okt.nouns(msg)   # 문서 중 명사만 얻기

#print(nouns)   # ['손아섭', '삼진', '콜', '당한', '후', '포수', ... 

result = [] # 두 글자 이상의 단어만 저장
for imsi in nouns:
    if len(imsi) > 1:
        result.append(imsi)
        
print(result)
count = Counter(result) # from collections import Counter
tag = count.most_common(100)   # 상위 100개만 작업에 참여 #Counter(result).most_common(50)
print(tag)

import pytagcloud   # 워드 클라우드 만들기
taglist = pytagcloud.make_tags(tag, maxsize = 100)
print('taglist : ', taglist)

pytagcloud.create_tag_image(taglist, output='word.png', size=(1000, 600),               
                            background=(0,0,0), fontname='Korean', rectangular=False)  # 그리고 font.json에서 
# 한글 폰트가 깨지므로 C:\anaconda3\Lib\site-packages\pytagcloud\fonts에 맑은 고딕 넣어줘야함. 
# 그리고 font.json에서 {
#     "name": "Korean",
#     "ttf": "malgun.ttf",
#     "web": "http://fonts.googleapis.com/css?family=Nobile"
# }, 을 넣어주거나 바꿔준다.

# 이미지 읽기
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#%matplotlib inline     # jupyter에서 선언하면 show() 안해도 된다.

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()

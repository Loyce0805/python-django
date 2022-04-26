# 멀티프로세싱을 위한 웹 스크래핑

# 멀티프로세싱 X
# https://beomi.github.io/beomi.github.io_old/ 사이트의 컨텐츠를 scraping
import requests
from bs4 import BeautifulSoup as bs
import time

from multiprocessing import Pool

def get_link():   # 제목 a tag 읽기
    data = requests.get('https://beomi.github.io/beomi.github.io_old/').text
    soup = bs(data, 'html.parser')    #data = requests.get을 읽어서 parsing을 함
    my_titles = soup.select(
            'h3 > a'
        )
    
    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
    
    return data

def get_content(link):
    # print(link)
    abs_link = 'https://beomi.github.io' + link
    # print(abs_link)
    data = requests.get(abs_link).text
    soup = bs(data, 'html.parser')
    # 가져온 데이터로 뭔가를 할 수 있다. ...
    print(soup.select('h1')[0].text)  # 첫번째 h1 tag의 문자열을 출력
    
    
if __name__ == '__main__':
    startTime = time.time()
    """
    # print(get_link())
    # print(len(get_link()))
    for link in get_link():
        get_content(link)
    """
    
    pool = Pool(processes = 4)      #병렬 처리
    pool.map(get_content, get_link())   # get_link의 갯수만큼 get_content를 호출
    
    print('---%s 초 ---'%(time.time() - startTime))
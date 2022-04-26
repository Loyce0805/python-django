'''
Created on 2022. 4. 20.

'''
# xml 문서 처리
from bs4 import BeautifulSoup

with open('../testdata/my.xml', mode = 'r', encoding='UTF-8') as f:
    xmlfile = f.read()
    
print(xmlfile, type(xmlfile)) # <class 'str'>

soup = BeautifulSoup(xmlfile, 'lxml')
print(soup, type(soup))       # <class 'bs4.BeautifulSoup'>
print(soup.prettify())  # 이쁘게 보이게 하기

itemTag = soup.findAll('item')
print(itemTag[0])

print()
nameTag = soup.findAll('name')
print(nameTag[0]['id'])  # ['id']를 통해 id만 볼 수 있음.
print()
for i in nameTag:
    print(i['id'])
    
print('-------------------------')
for i in itemTag:
    nameTag = i.findAll('name')
    for j in nameTag:
        print('id:' + j['id'] + ', name: '+ j.string)
    tel = i.find('tel')
    print('tel : ' + tel.string)
    for j in i.find_all('exam'):
        print('kor:' + j['kor'] + ', eng:' + j['eng'])

print('-- 기상청 제공 날씨 정보 읽기-----------------------')
try:
    import urllib.request as req
    from bs4 import BeautifulSoup
    import pandas as pd
    url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
    plainText = req.urlopen(url).read().decode('UTF-8')
    # print(plainText)
    
    soup = BeautifulSoup(plainText, 'lxml')
    # print(soup)
    title = soup.find('title').string
    print(title)
    
    # wf = soup.find('wf')
    # print(wf)
    city = soup.find_all('city')
    # print(city)
    cityDatas = []
    for c in city:
        cityDatas.append(c.string)
    df = pd.DataFrame()
    df['city'] = cityDatas
    # print(df)
    tempMins = soup.select("location > province + city + data > tmn")  # +는 형제(sibling)이고 아래방향임, -는 위방향
    print(tempMins)
    tempDatas = []
    for t in tempMins:
        tempDatas.append(t.string)
    df['temp_min'] = tempDatas
    df.columns = ['지역', '최저기온']
    print(df.head(3))
    print(df.tail(3))
    
    # df 를 파일로 저장
    df.to_csv("날씨.csv", index = False)
    # print(pd.read_csv("날씨.csv"))
    
    print('----')
    print(df[0:3])
    print(df[-3:len(df)])
    
    print()
    print(df.iloc[0], type(df.iloc[0])) # 하나만 뽑았기 때문에 타입이 Series
    
    print()
    print(df.iloc[0:2, :])  # 행은 0~2까지, 열은 모두다
    print(df.iloc[0:2, 0:1])
    print(df.iloc[0:2, 0:2])
    
    print()
    print(df.loc[0:2])  # loc는 iloc와 다르게 라벨명을 쓸 수 있다.
    print(df.loc[[0, 2]])   # 0행, 2행만 나오게
    
    print()
    print(df.loc[0:2, ['최저기온', '지역']]) # 열을 바꿔서 할수 있다.
    
    print()
    print(df['최저기온'].mean())     # 최저기온 평균
    print(df['최저기온'].describe()) # 요약 통계량( 갯수, 중복 등등)
    
    print()
    df = df.astype({'최저기온':int})     # astype을 이용해서 int로 바꿔준다.
    print(df.loc[df['최저기온'] >= 15])  # string이기 떄문에 비교가 안됨.
    print(df.loc[(df['최저기온'] >= 10) & (df['최저기온'] <= 12)])  # 10도이상 12도 이하만 나온다.
    
    print()
    print(df.sort_values(['최저기온'], ascending=True)) # ascending으로 오름차순 분류
    
except Exception as e:
    print('err : ', e)



'''Created on 2022. 4. 20. 6교시! '''
# 웹에서 JSON 문서 읽기

import json
import urllib.request as req

url = "http://127.0.0.1:8888/library.json"

libdata = req.urlopen(url).read().decode()
print(libdata, type(libdata))   # <class 'str'>

jsondata = json.loads(libdata)
print(jsondata, type(jsondata)) # <class 'dict'>

print()
print(jsondata['row'][0]['LIBRARY_NAME'])

# dict의 기능을 이용해 원하는 자료 얻기
libData = jsondata.get('row')
print(libData)

name = libData[0].get('LIBRARY_NAME')  # 위에 jsondata['row'][0]['LIBRARY_NAME'] 와 동일
print(name)

datas = []
for ele in libData:
    name = ele.get('LIBRARY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name + " " + tel + " " + addr)
    imsi = [name, tel, addr]
    datas.append(imsi)

print('---')
import pandas as pd
df = pd.DataFrame(datas, columns=['도서관명', '전화', '주소'])
print(df)
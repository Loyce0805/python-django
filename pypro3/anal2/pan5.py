'''
Created on 2022. 4. 19. 16:00

'''

# file i/o
import pandas as pd
# 읽기
df = pd.read_csv('../testdata/ex1.csv')
print(df, type(df))  # <class 'pandas.core.frame.DataFrame'>

print()
print(pd.read_table('../testdata/ex1.csv', sep=',', skipinitialspace=True))  
# skipinitialspace : 공백이 있으면 제거

print()
print(pd.read_csv('../testdata/ex2.csv', header=None))
print(pd.read_csv('../testdata/ex2.csv', header=None, names=list('korea')))

print()
print(pd.read_csv('../testdata/ex3.txt'))
print(pd.read_csv('../testdata/ex3.txt').describe())
print(pd.read_csv('../testdata/ex3.txt', sep='\s+'))   # sep = ' '  띄어쓰기를 기준으로 나눠줌.
print(pd.read_csv('../testdata/ex3.txt', sep='\s+').describe())
print(pd.read_csv('../testdata/ex3.txt', sep='\s+', skiprows=[1, 3]))  # 1행하고 3행은 빼는 skiprows

print()
print(pd.read_fwf('../testdata/data_fwt.txt', header=None, 
                  widths=(10, 3, 5), names=('date', 'name', 'price'), encoding='UTF-8'))  \
                  # widths가 10자리, 3자리, 5자리로 나눠줌.

print()
# chink : 대 용량의 파일인 경우에는 chunk 단위로 부분 씩 읽어들일 수 있다.
test = pd.read_csv("../testdata/data_csv2.csv")
print(test)
print()
test2 = pd.read_csv("../testdata/data_csv2.csv", header=None, chunksize=3)
print(test2)  # TextFileReader object

for p in test2:
    # print(p)
    print(p.sort_values(by=2, ascending = True))   # 2번째 칼럼을 내림차순으로 정렬해서 chunk 단위로 보여줌
    
print('----저장-----')
items = {'apple':{'count':10, 'price':1500}, 'orange':{'count':5, 'price':1000}}
df = pd.DataFrame(items)
print(df)
# df.to_clipboard()   # 클립보드로 저장(컨트롤 C 컨트롤 V처럼)
# print(df.to_html)   # html 양식으로 장고에 휙 던지면 된다.
# print(df.to_json)
print(df.to_xml())

df.to_csv('pan5ex1.csv', sep=',')
df.to_csv('pan5ex1.csv', sep=',', index=False)  # 색인은 제외
df.to_csv('pan5ex1.csv', sep=',', index=False, header=False) # 색인, 칼럼명은 제외

# 기타 다른 파일 형식으로 저장 가능
'''
Created on 2022. 4. 19.

@author: Jain
'''
import pandas as pd
import numpy as np

# pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.
#   데이터 : http://cafe.daum.net/flowlife/RUrO/103
#             https://github.com/pykwon/python/blob/master/testdata_utf8/titanic_data.csv
#
#     titanic_data.csv 파일을 다운로드 후
#    df = pd.read_csv('파일명',  header=None,,,)  
#
#  1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
#       cut() 함수 사용
#      bins = [1, 20, 35, 60, 150]
#       labels = ["소년", "청년", "장년", "노년"]
#
#   2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
#       df.pivot_table()
#      index에는 성별(Sex)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
#       출력 결과 샘플1 :       
# pclass    1    2    3
# sex            
# female    0.968085    0.921053    0.500000
# male    0.368852    0.157407    0.135447
#
#    index에는 성별(Sex) 및 나이(Age)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
#    출력 결과 샘플2 : 위 결과물에 Age를 추가. 백분율로 표시. 소수 둘째자리까지.    예: 92.86
    
# df3 = pd.read_csv("../testdata/titanic_data.csv", header=None)
df3 = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(df3.head(3))

bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df3.Age = pd.cut(df3.Age, bins, labels = labels)
print(df3.Age)
print('1) \n', df3.Age.value_counts())

print()
df3_n=df3.pivot_table(index = ['Sex'], columns = 'Pclass',
                    values = 'Survived', fill_value = 0)
print('2) \n', round(df3_n * 100, 2))


# pandas 문제 4)
#  https://github.com/pykwon/python/tree/master/testdata_utf8
#
#  1) human.csv 파일을 읽어 아래와 같이 처리하시오.
#      - Group이 NA인 행은 삭제
#      - Career, Score 칼럼을 추출하여 데이터프레임을 작성
#      - Career, Score 칼럼의 평균계산
#      참고 : strip() 함수를 사용하면 주어진 문자열에서 양쪽 끝에 있는 공백과 \n 기호를 삭제시켜 준다. 
#              그래서 위의 문자열에서 \n과 오른쪽에 있는 공백이 모두 사라진 것을 확인할 수 있다. 
#              주의할 점은 strip() 함수는 문자열의 양 끝에 있는 공백과 \n을 제거해주는 것이지 중간에 
#              있는 것까지 제거해주지 않는다.
human_df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')
print(human_df.head(2))
print(human_df.info())

human_df = human_df.rename(columns=lambda x: x.strip())
human_df['Group'] = human_df['Group'].str.strip()
human_df = human_df[human_df['Group']!='NA']
print(human_df.head(5),"\n")

cs_df = human_df[human_df.columns[2:4]]
print(cs_df.head(5), "\n")
print(cs_df.mean())

# 2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
#      - 파일 정보 확인
#      - 앞에서 3개의 행만 출력
#      - 요약 통계량 보기
#      - 흡연자, 비흡연자 수를 계산  : value_counts()
#      - 요일을 가진 칼럼의 유일한 값 출력  : unique()
#           결과 : ['Sun' 'Sat' 'Thur' 'Fri']


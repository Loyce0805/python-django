'''
Created on 2022. 5. 2. 상관관계 분석
'''
# 공공 데이터(외국인 관광객 서울 관광지 관련)로 상관관계 분석

import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rc('font', family='malgun gothic')

# 산점도 그래프 작성 함수 만들기
def setScatterGraph(tour_table, all_table, tourPoint):
    # print(tourPoint)    #창덕궁, 운현궁, 경복궁, 창경궁, 종묘
    # 계산할 관광지명에 해당하는 데이터만 뽑아 tour 변수에 저장하고 외국인 자료와 병합
    tour = tour_table[tour_table['resNm'] == tourPoint]
    # print(tour)
    merge_table = pd.merge(tour, all_table, left_index = True, right_index = True)
    # print(merge_table)
    
    # 시각화
    fig = plt.figure()
    fig.suptitle(tourPoint + ' 상관관계분석')

    # 중국인
    plt.subplot(1, 3, 1)
    plt.xlabel('중국인 입국 수')
    plt.ylabel('외국인 입장객 수')
    lamb1 = lambda p:merge_table['china'].corr(merge_table['ForNum'])
    r1 = lamb1(merge_table)
    print('r1:', r1)
    plt.title('r={:.3f}'.format(r1))
    plt.scatter(merge_table['china'], merge_table['ForNum'], s=6, c='red', alpha=0.8) # s는 scale(크기), c는 color(색깔), alpha는 투명도
    
    # 일본인
    plt.subplot(1, 3, 2)
    plt.xlabel('일본인 입국 수')
    plt.ylabel('외국인 입장객 수')
    lamb2 = lambda p:merge_table['japan'].corr(merge_table['ForNum'])
    r2 = lamb2(merge_table)
    print('r2:', r2)
    plt.title('r={:.3f}'.format(r2))
    plt.scatter(merge_table['japan'], merge_table['ForNum'], s=6, c='green', alpha=0.8)
    
    # 미국인
    plt.subplot(1, 3, 3)
    plt.xlabel('미국인 입국 수')
    plt.ylabel('외국인 입장객 수')
    lamb3 = lambda p:merge_table.usa.corr(merge_table['ForNum'])
    r3 = lamb3(merge_table)
    print('r3:', r3)
    plt.title('r={:.3f}'.format(r3))
    plt.scatter(merge_table.usa, merge_table['ForNum'], s=6, c='blue', alpha=0.8)
    
    plt.tight_layout()  # 열(plot) 간에 공백을 만들어준다.
    plt.show()
    
    return [tourPoint, r1, r2, r3]  #관광지명과 상관계수 3개가 리턴 됨.

def chulbal():
    # 서울시 관광지 정보 파일 읽기
    fname = "../testdata/서울시_관광지.json"
    jsonTP = json.loads(open(fname, mode='r', encoding = 'utf-8').read())   # str -> dict : json decoding
    # print(jsonTP, type(jsonTP)) # <class 'list'> : List[]로 dict{}를 감쌌다.
    tour_table = pd.DataFrame(jsonTP, columns = ('yyyymm', 'resNm', 'ForNum')) # 년월, 관광지명, 입장객수
    tour_table = tour_table.set_index('yyyymm')
    # print(tour_table[:2])   # 201101   창덕궁   14137 ...
    
    resNm = tour_table.resNm.unique()   # nunique는 갯수만 보여준다.
    # print('관광지명 : ', resNm[:5])     # ['창덕궁' '운현궁' '경복궁' '창경궁' '종묘']
    
    # 중국인 정보
    cdf = '../testdata/중국인방문객.json'
    jdata = json.loads(open(cdf, 'r', encoding = 'utf-8').read())
    # print(jdata)
    china_table = pd.DataFrame(jdata, columns = ('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns = {'visit_cnt':'china'})   # visit_cnt 칼럼명을 china로 바꿈
    china_table = china_table.set_index('yyyymm')
    print(china_table[:2])
    
    # 일본인 정보
    jdf = '../testdata/일본인방문객.json'
    jdata = json.loads(open(jdf, 'r', encoding = 'utf-8').read())
    japan_table = pd.DataFrame(jdata, columns = ('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns = {'visit_cnt':'japan'})   #visit_cnt 칼럼명을 japan로 바꿈
    japan_table = japan_table.set_index('yyyymm')
    print(japan_table[:2])
    
    # 미국인 정보
    udf = '../testdata/미국인방문객.json'
    jdata = json.loads(open(udf, 'r', encoding = 'utf-8').read())
    usa_table = pd.DataFrame(jdata, columns = ('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns = {'visit_cnt':'usa'})   #visit_cnt 칼럼명을 usa로 바꿈
    usa_table = usa_table.set_index('yyyymm')
    print(usa_table[:2])
    
    all_table = pd.merge(china_table, japan_table, left_index=True, right_index = True) # Index를 기준으로 left join, right join 해주기
    all_table = pd.merge(all_table, usa_table, left_index=True, right_index = True) 
    print(all_table[:3])
    
    r_list = []
    for tourPoint in resNm[:5]: # 관광지 5번을 반복해서 setScatterGraph 호출
        r_list.append(setScatterGraph(tour_table, all_table, tourPoint)) # r_list에 setScatterGraph를 추가
    
    # print(r_list)   # [['창덕궁', -0.05879110406006314, 0.2774443570141011, 0.4028160633050156], ... matrix로 받아옴
    r_df = pd.DataFrame(r_list, columns = ('고궁명', '중국' ,'일본', '미국')) #matrix인 r_list를 데이터프레임으로 받음
    r_df = r_df.set_index('고궁명')    #고궁명 으로 인덱싱 함
    print('r_df\n', r_df)
    
    r_df.plot(kind = 'bar', rot = 60)
    plt.show()
    

if __name__ == '__main__':
    chulbal()
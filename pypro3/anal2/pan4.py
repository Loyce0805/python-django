import numpy as np
import pandas as pd

df = pd.DataFrame(1000 + np.arange(6).reshape(2,3), index=['대전','서울'], 
                  columns=['2020', '2021', '2022'])
print(df)

print()
df_row = df.stack()  # index를 기준으로 열 쌓기
print(df_row)
df_col = df_row.unstack()   # stack 결과 원복
print(df_col)

print('범주화(연속형데이터를 범주형으로 바꿔준다. ------------------')
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]   # 구간 기준 값
result_cut = pd.cut(price, cut)
print(result_cut) # [(9, 11], (3, 7], (7, 9], (3, 7]]   (a, b] <== a초과 b 이하   a < x <= b
print(pd.value_counts(result_cut))

print()
datas = pd.Series(np.arange(1, 1001))
print(datas.head(2))
print(datas.tail(2))

cut2 = [0, 300, 600, 1000]
result_cut2 = pd.cut(datas, cut2)
print(result_cut2)


result_cut3 = pd.qcut(datas, 3)   # 지정한 숫자만큼 범주화
print(result_cut3)
print(pd.value_counts(result_cut3))

print()
# 그룹화
group_col = datas.groupby(result_cut3)
print('----')
print(group_col)    # SeriesGroupBy object
print(group_col.agg(['count', 'mean', 'std', 'min']))  # pandas:agg('함수명') 함수를 실행하는 메소드

print()
# 함수 작성
def summaryFunc(gr):
    return {
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min()
    }
    
print(group_col.apply(summaryFunc))

print()
print(group_col.apply(summaryFunc).unstack())

print('DataFrame자료 합치기 ------------')
df1 = pd.DataFrame({'data1':range(7), 'key':['b', 'b', 'a', 'c', 'a', 'a', 'b']})
print(df1)
df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2':range(3)})
print(df2)
print()
print(pd.merge(df1, df2, on='key'))  # 'key'를 기준으로 병합. inner join : 교집합

print()
print(pd.merge(df1, df2, on='key', how='inner'))

print()
print(pd.merge(df1, df2, on='key', how='outer'))  # full outer join

print()
print(pd.merge(df1, df2, on='key', how='left'))   # left outer join

print()
print(pd.merge(df1, df2, on='key', how='right'))  # right outer join

# 공통 칼럼이 없는 경우 merge
print()
df3 = pd.DataFrame({'key2':['a', 'b', 'd'], 'data2':range(3)})
print(df3)
print(pd.merge(df1, df3, left_on='key', right_on='key2'))

print('--concat : 자료 이어 붙이기--')
print(pd.concat([df1, df3]))
print(pd.concat([df1, df3], axis = 0))   # 행단위(기본)
print(pd.concat([df1, df3], axis = 1))   # 열단위

print('DataFrame 관련 집계 메소드 : pivot, groupby, pivot_table ---------')
data = {'city':['강남', '강북', '강남', '강북'],
        'year':[2000, 2001, 2002, 2002],
        'pop':[3.3, 2.5, 3.0, 2.0]}
df = pd.DataFrame(data)
print(df)
print('pivot : df.pivot(index, columns, values)---')
print(df.pivot('city', 'year', 'pop'))  # 구조를 재구성
print(df.pivot('year', 'city', 'pop'))

print()
print(df.set_index(['year', 'city']).unstack())

print('groupby : 특정 칼럼을 기준으로 그룹화해서 소계---')
hap = df.groupby(['city'])
print(hap) # DataFrameGroupBy object
print(hap.sum())

print(df.groupby(['city']).sum()) # 위 소스 코드를 한 줄로 표현
print(df.groupby(['city']).agg('sum'))
print(df.groupby(['city', 'year']).mean())

# 피벗 테이블(pivot table)은 커다란 표(예: 데이터베이스, 스프레드시트, 비즈니스 인텔리전스 프로그램 등)의 
# 데이터를 요약하는 통계표이다. 이 요약에는 합계, 평균, 기타 통계가 포함될 수 있으며 피벗 테이블이 
# 이들을 함께 의미있는 방식으로 묶어준다. 피벗 테이블은 데이터 처리의 한 기법이다. 
# 유용한 정보에 집중할 수 있도록 하기 위해 통계를 정렬 또는 재정렬(피벗)한다.

print('pivot_table : pivot과 groupby 기능을 모두 사용 가능---')
print(df)
print(df.pivot_table(index=['city']))  # 기본 함수는 평균을 보여줌.(mean)
print(df.pivot_table(index=['city'], aggfunc=np.mean))  #  aggfunc=np.mean이 기본값

print(df.pivot_table(index=['city', 'year'], aggfunc=[len, np.sum]))

print(df.pivot_table(values=['pop'], index=['city']))   # city별 pop(column)의 평균

print(df.pivot_table(values=['pop'], index=['city'], aggfunc=len))   # city별 pop(column)의 건 수 

print(df.pivot_table(values=['pop'], index=['year'], columns=['city'], aggfunc=np.mean))

print(df.pivot_table(values=['pop'], index=['year'], columns=['city'],
                     aggfunc=np.mean, margins=True))

print(df.pivot_table(values=['pop'], index=['year'], columns=['city'],
                     aggfunc=np.mean, margins=True, fill_value=0))

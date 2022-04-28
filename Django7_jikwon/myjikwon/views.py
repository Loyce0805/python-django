from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from myjikwon.models import Jikwon
plt.rc('font', family = 'malgun gothic') # 한글 호환

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def showFunc(request):
    jikwons = Jikwon.objects.all().values()   # 0001_initial.py 에 있는 Jikwon data를 불러온다.  # values를 붙이면 list안에 dicttype으로 들어간다. QuerySet이다.
    print(jikwons)  # <QuerySet [{'jikwon_no': 1, 'jikwon_name': '홍길동', 'buser_num': 10....
    df = pd.DataFrame.from_records(jikwons)
    df.columns = ['사번', '직원명', '부서', '직급', '연봉', '입사', '성별', '평점']
    print(df.head(2))
    
    # 부서별 연봉합/평균
    buser_group = df['연봉'].groupby(df['부서'])  # groupby말고 pivot도 있다
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    print(buser_group_detail, type(buser_group))  # buser_group은 Series타입, buser_group_detail은 dict타입
 
    # 부서별 연봉합/평균 -> DataFrame으로 변환해서 하기
    print('df2---------------')
    df2 = pd.DataFrame(buser_group_detail)
    print(df2)          
    
    # 시각화 이미지로 저장
    bu_result = buser_group.agg(['sum', 'mean'])
    print(bu_result, type(bu_result))  # bu_result는 DataFrame
    
    bu_result.plot(kind='barh')
    plt.title('부서별 연봉합/평균')
    plt.xlabel('연봉')
    fig = plt.gcf()
    fig.savefig('Django7_jikwon/myjikwon/static/images/buser.png')
    
    return render(request, 'list.html', 
                  {'datas':df.to_html(index = False),   # dataframe과 table은 .to_html로 넘길 수 있다.
                   'buser_group':buser_group_detail,    # 다른 애들은 DataFrame으로 만들어서 넘기던가 다른 방식으로 넘겨야함.
                   'buser_group2':df2.to_html()})       # buser_group을 DataFrame으로 변환한 뒤 to_html 이용
    

from django.shortcuts import render, redirect
from myguest.models import Guest
from datetime import datetime
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.

def mainFunc(request):
    return render(request, 'main.html')   # forwarding : 서버에서 서버 파일 직접 호출

def ListFunc(request):
    print(Guest.objects.filter(title__contains = '반가워'))  # 얘는 true,false랑 값 가져오는거 둘다
    print(Guest.objects.filter(id = 1))
    print(Guest.objects.filter(title = '문안인사'))   # where 조건이라고 보면 됨.
    print(Guest.objects.get(id = 1))  # get은 id=1인거 하나만 읽어오기
    
    gdatas = Guest.objects.all()  # 전체자료 읽기
    # gdatas = Guest.objects.all().order_by('title')              # 정렬(asscending sort)
    # gdatas = Guest.objects.all().order_by('-title')             # 정렬(descending sort)
    # gdatas = Guest.objects.all().order_by('-id', 'title')[0:2]  # 정렬(id:descending, title:asscending sort) 0~1까지 2개만 나옴.
    
    return render(request, 'list.html', {'gdatas':gdatas}) # list.html과 동시에 gdatas라는 키에 gdatas라는 값을 넣어서 같이 넘겨줌

def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == "POST":
        # print(request.POST.get("title"))
        # print(request.POST["title"]) # 둘다 똑같다. 만약 get이라면 Post가 아니라 get으로
        Guest(
            title = request.POST.get("title"), # title은 table의 칼럼명, "title"은 insert.html에 있는 name변수명
            content = request.POST.get("content"),
            regdate = datetime.now()  # from django.utils import timezone 이후 timezone.now() 써도 됨.
        ).save() # insert into ... 구문 id는 자동 증가하므로 title만
        
    #return HttpResponseRedirect('/guest')     # 추가 후 목록 보기 redirect 방식 : 클라이언트를 통해 자료 요청
    return redirect('/guest') # shortcuts의 redirect import

""" 수정하기
gtab = Guest.objects.get(id=해당아이디)
gtab.title = '수정제목'
gtab.content = '수정내용'
gtab.save()    "update 테이블명 set ....
"""

"""삭제
gtab = Guest.objects.get(id=해당아이디)
gtab.delete()  "delete from 테이블명 ...
"""

from django.shortcuts import render
from dbapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    datas = Article.objects.all() # Django의 ORM을 사용 select * from article # dbapp.models Import 하기
    print(datas, type(datas))
    print(datas[0].name)
    
    return render(request, 'list.html', {'articles':datas}) # {'articles':datas}로 QuerySet을 전달
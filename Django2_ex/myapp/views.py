from django.shortcuts import render
from django.http.response import HttpResponseRedirect


# Create your views here.

def mainFunc(request):
    return render(request, 'main.html')

def showFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request, 'show.html')
    
    elif request.method == 'POST':
        print('POST 요청 처리')
        gen = request.POST.get('gender')
        return render(request, 'showlist.html', {'gen':gen})
    else:
        print('요청에러')
    
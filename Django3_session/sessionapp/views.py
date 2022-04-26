from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def setosFunc(request):
    #print('request GET : ', request.GET)      #<QueryDict: {}>
    
        if "favorite_os" in request.GET:
        print('request GET : ', request.GET["favorite_os"])
        # request.session['세션키']
        
        request.session['f_os'] = request.GET["favorite_os"]     # f_os라는 key로 session을 생성
        return HttpResponseRedirect("/showos")       #  redirect 방식  (client 컴을 통해 요청을 함)
    else:
        return render(request, 'selectos.html')     # forward 방식 (sever가 직접 file을 선택해 client로 전송)
    
def showosFunc(request):
    dict_context = {}
    
    if "f_os" in request.session:
        print('유효 시간 : ', request.session.get_expiry_age())
        dict_context['select_os'] = request.session['f_os']
        dict_context['message'] = "그대가 선택한 운영체제는 %s"%request.session['f_os']
    else:
        dict_context['select_os'] = None
        dict_context['message'] = "운영체제를 선택하지 않았어요"
    
    # del request.session['f_os']    # 세션 삭제
    request.session.set_expiry(5)  #  세션 유효시간을 5초로 제한
    
    return render(request, 'show.html', dict_context)  

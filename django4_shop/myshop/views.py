from django.shortcuts import render
from flask.globals import session

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")

def page1Func(request):
    return render(request, "page1.html")

def page2Func(request):
    return render(request, "page2.html")

def cartFunc(request):
    name = request.POST["name"]
    price = request.POST["price"]
    print(name, price)
    product = {'name':name, 'price':price}
    
    productList = []
    if "shop" in request.session:
        productList = request.session['shop']
        request.append(product)
        request.session['shop'] = productList
    else:
        productList.append(product)
        request.session['shop'] = productList
        
    print(productList)
    context = {}   # html에 보낼 용도
    context['products'] = request.session['shop']
    return render(request, 'cart.html', context)


def buyFunc(request):
    if "shop" in request.session:
        productList = request.session['shop']
        print(productList)
        
        total = 0
        for pro in productList:
            total += int(pro['price'])
        print(total)
        request.session.clear()     # session 안의 모든 키 삭제(장바구니 내용 다 지움. 결제를 했기 떄문에)
    
    return render(request, 'buy.html', {'total' : total })
        
            








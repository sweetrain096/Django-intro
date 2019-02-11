import random
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print(request)
    print(type(request))
    print(request.META)
    return render(request, "index.html")
    
def dinner(request):
    box = ["치킨", "충만치킨", "엽떡", "초밥"]
    pick = random.choice(box)
    # return HttpResponse(f"오늘 저녁은 {pick}!!")
    # render 필수인자.
    # 1) request, 2) template 파일(html)
    # render 선택인자.
    # 3) dictionary : 템플릿에서 쓸 변수 값을 정의
    return render(request, "dinner.html", {'dinner' : pick, 'box' : box})
    # return ('dinner.html', dinner = dinner, box = box)
    # template은 기본적으로 문법이 jinja2와 같은데(비슷), 장고에서는 DTL을 쓴다.
    # Django Template Language

def you(request, name):
    return render(request, 'you.html', {'name' : name})

def cube(request, num):
    # num = int(num)
    return render(request, 'cube.html', {'num' : num, 'cube' : num ** 3})
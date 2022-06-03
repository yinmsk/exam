from django.shortcuts import render

# Create your views here.

def caffee(request, ):
    if request.method == 'GET':



    elif request.method == 'POST':
        menus = [{"caffee_01": '카푸치노, 아라비카노, 아프리카노'}], [{"caffee_02": '카페라때, 라때, 믹스커피'}], [{"caffee_03": '에이드, 물, 오랜지 쥬스'}]

    return render(request, 'exam.html', menus)
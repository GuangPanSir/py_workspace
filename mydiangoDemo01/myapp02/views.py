from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def testReader(request):
    print("sessio n中的数据" + request.session.get("userAccount"))
    context = dict()  # 字典
    context["name"] = '张三'
    context["hobby"] = ['吃', '旅游']
    return render(request, 'testReader.html', context)


# 响应重定向 新发起请求 可以是任何可以访问的url
def testRedirct(request):
    return redirect("http://localhost:8080/")


"""
模板中复杂数据展示
"""


def testTemplate(request):
    context = dict()  # 创建字典
    context['userInfo'] = {'name': 'lucy', 'age': 18, 'sex': 'male'}
    context['infos'] = [{'name': 'lucy', 'age': 17, 'sex': 'female', 'hobby': ['eat', 'climb']},
                        {'name': 'Bob', 'age': 18, 'sex': 'male', 'hobby': ['games', 'basketball', 'pingpong']},
                        {'name': 'snaky', 'age': 19, 'sex': 'female', 'hobby': ['dance', 'piano']}]
    return render(request, "testTemplate.html", context)

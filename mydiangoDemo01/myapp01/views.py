import datetime

from django.shortcuts import render
from userApp.models import *
from userApp.service import service

# 请求转发

# Create your views here.

'''
定义视图函数
'''


def test(request):
    print("123456")
    return render(request, "test.html")


def loginPage(request):
    return render(request, 'login.html')


'''
页面访问
pageName 页面名 模板名
访问此页面，地址栏有参数  --Restful 风格
'''


def toPage(request, page_name):
    return render(request, page_name)


# 登录操作
def login(request):
    # 获取客户提交的数据 get请求方式
    user_acc = request.GET.get('userAcc', None)  # 获得登录请求的信息
    user_pass = request.GET.get('userPass', None)
    login_user = service.login(user_acc, user_pass)
    if login_user:
        print(login_user)
        request.session['login_user'] = login_user.userId
        # 查询商品名称中带某个字段的数据
        pros = Products.objects.filter(proName__contains='瓜')
        return render(request, 'main.html', {'pros': pros})
    else:
        return render(request, 'login.html', context={'error': "账号或密码错误"})


def register(request):
    user_acc = request.POST.get('userAcc')  # 获取注册信息
    # 判断用户账号是否存在
    if not service.accountIsExit(user_acc):
        user_pass = request.POST.get('userPass')
        user_sex = request.POST.get('userSex')
        user_add = request.POST.getlist('address')  # 一个参数多个值的获取
        user_obj = UserInfo()
        user_obj.userId = service.createUserId()
        user_obj.userAccount = user_acc
        user_obj.userPass = user_pass
        user_obj.userSex = user_sex
        user_obj.userBirth = datetime.date(1997, 9, 14)
        user_obj.save()  # 添加数据，有则修改，无则添加
        return render(request, 'test.html')
    return render(request, "register.html")


def show_user_goods(request):
    user = UserInfo.objects.get(userId=request.session.get('login_user'))
    # 获取当前用户的购物车物品
    products = user.pros.all()
    cont = {'pros': products}
    return render(request, 'shoppingCar.html', cont)

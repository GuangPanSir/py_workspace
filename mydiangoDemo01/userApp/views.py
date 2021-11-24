import time

from django.shortcuts import render

# Create your views here.

# 测试数据添加
from mydiangoDemo01.userApp.models import UserInfo, OrderInfo, Products


def userReg(request):
    UserInfo.objects.create(userId=2, userAccount='wangbing', userPass='123456')  # 创建并保存对象
    return render(request, "userTest.html")


# 返回订单编号的时间信息
def idInfo():
    # 获得当前系统时间并进行格式化
    idinfo = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return idinfo


def orderAdd(request):
    # 查询这个账号密码的用户
    # 条件查询
    user = UserInfo.objects.filter(userAccount='Nacy', userPass='123456')[0]
    OrderInfo.objects.create(orderId=str(user.userId) + idInfo(), orderMon=123.5, userInfo=user)
    return render(request, "userTest.html")


def userAddGoods(request):
    # pro_id = request.GET.get('pro_id')
    # # 获得一个商品对象
    # pro = Products.objects.get(proId=int(pro_id))
    # # 获得一个对象集
    # user = UserInfo.objects.filter(userId=request.session.get('login_user'))[0]
    # # 添加一条数据
    # # 用户添加一个商品
    # user.pros.add(pro)
    # # UserGoods.objects.create(user=userObj, pro=pro)
    # return render(request, "main.html")
    pro_id_infos = request.GET.getlist('proId')
    print(pro_id_infos)
    user = UserInfo.objects.filter(userId=request.session.get('login_user'))[0]
    for pro_id_info in pro_id_infos:
        pro = Products.objects.get(proId=int(pro_id_info))
        user.pros.add(pro)
    return render(request, "main.html")


def delete_goods(request):
    pro_id_info = request.GET.get('proId')
    pro = Products.objects.get(proId=int(pro_id_info))
    user = UserInfo.objects.get(userId=request.session.get('login_user'))
    user.pros.remove(pro)
    return render(request, "main.html")


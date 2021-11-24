from django.db import models


# Create your models here.
class UserInfo(models.Model):
    #  属性定义
    userId = models.BigIntegerField(primary_key=True)
    userAccount = models.CharField(max_length=50, unique=True)
    userPass = models.CharField(max_length=50)
    userBirth = models.DateField(null=True)
    userSex = models.CharField(max_length=4)
    # 建立用户商品的多对多关系
    pros = models.ManyToManyField("Products", db_table='usergoodstable')

    class Meta:
        db_table = 'userInfoTable'

    pass


class OrderInfo(models.Model):
    orderId = models.CharField(primary_key=True, max_length=100)
    orderDate = models.DateTimeField(auto_now=True)
    orderMon = models.FloatField()
    userInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 设置外键

    class Meta:
        db_table = 'orderTable'


class Products(models.Model):
    proId = models.BigAutoField(primary_key=True)  # 自增长
    proName = models.CharField(max_length=200)
    proPrice = models.FloatField(default=0.0)
    proImg = models.CharField(max_length=200)

    class Meta:
        db_table = 'productsTable'


# 用户购物车，多对多的设置
# 两种方式创建多对多的方式
# class UserGoods(models.Model):
#     user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
#     pro = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
#
#     class Meta:
#         db_table = 'userGoodsTable'

"""mydiangoDemo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp01 import views as myViews
from myapp02 import views as myViews02
from userApp import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myViews.loginPage),
    path('test/', myViews.test),
    path('page/<str:pageName>', myViews.toPage),
    path('user/login/', myViews.login),
    path('user/register/', myViews.register),
    path('testReader/', myViews02.testReader),
    path('testRedirct/', myViews02.testRedirct),
    path("testTemplate/", myViews02.testTemplate),
    path("test/add/", userViews.userReg),
    path("test/orderadd/", userViews.orderAdd),
    path("test/adduserGoods", userViews.userAddGoods),
    path("test/deleteuserGoods", userViews.delete_goods),
    path("user/goods/", myViews.show_user_goods)
]

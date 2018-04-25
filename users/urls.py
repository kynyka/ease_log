# -*- coding: utf-8 -*-
'''为应用程序users定义URL模式'''
from django.conf.urls import url
from django.contrib.auth.views import login  # 先导入默认视图login

from . import views

urlpatterns = [
    # 登录页面
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),  # 登录页面的URL模式与URL http://localhost:8000/users/login/匹配【项目的总urls.py里已有修饰头users/】;视图实参login让它将请求发送给Django默认视图 login。鉴于我们没有编写自己的视图函数,我们传递了一个字典,告诉Django去哪里查找我们将编写的模板
    # 注销
    url(r'^logout/$', views.logout_view, name='logout'), # 此URL模式将请求发送给函数logout_view()。这样给这个函数命名,旨在将其与我们将在其中调用的函数logout()区分开来
    url(r'^register/$', views.register, name='register'),
]

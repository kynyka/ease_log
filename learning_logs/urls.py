# -*- coding: utf-8 -*-
'''定义learning_logs的URL模式'''
from django.conf.urls import url
from . import views  # 句点让Python从当前的urls.py模块所在的文件夹中导入views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),  # 实际的URL模式是一个对函数url()的调用,这个函数接受三个实参;第2个指定了要调用的视图函数。请求的URL与前面的正则匹配时,Django将调用views.index。第3个实参将这个URL模式的名称指定为index,让我们能在代码的其他地方引用它。每当需要提供到这个主页的链接时,我们都将使用这个名称,而不编写URL。
]

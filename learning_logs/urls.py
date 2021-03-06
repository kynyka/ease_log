# -*- coding: utf-8 -*-
'''定义learning_logs的URL模式'''
from django.conf.urls import url
from . import views  # 句点让Python从当前的urls.py模块所在的文件夹中导入views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),  # 实际的URL模式是一个对函数url()的调用,这个函数接受三个实参;第2个指定了要调用的视图函数。请求的URL与前面的正则匹配时,Django将调用views.index。第3个实参将这个URL模式的名称指定为index,让我们能在代码的其他地方引用它。每当需要提供到这个主页的链接时,我们都将使用这个名称,而不编写URL。

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),  # Django检查请求的URL时，这个模式与这样的URL匹配：基础URL后面跟着 topics 。可以在末尾包含斜杠，也可以省略它，但单词 topics 后面不能有任何东西，否则就与该模式不匹配。其URL与该模式匹配的请求都将交给views.py中的函数 topics() 进行处理。
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),  # "?P<topic_id>"将匹配的值存储到topic_id中;发现URL与这个模式匹配时，Django将调用视图函数topic(),并将存储在topic_id中的值作为实参传递给它

    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),  # 这个URL模式将请求交给视图函数new_topic(),接下来我们将编写这个函数

    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

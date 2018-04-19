# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Topic  # 首先导入与所需数据相关联的模型

# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/index.html')  # 第1个实参为原始请求对象,第2个实参为可用于创建网页的模板

def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}  # 我们定义了一个将要发送给模板的上下文。上下文是一个字典，其中的键是我们将在模板中用来访问数据的名称，而值是我们要发送给模板的数据。在这里，只有一个键—值对，它包含我们将在网页中显示的一组主题。创建使用数据的网页时，除对象 request 和模板的路径外，我们还将变量 context 传递给 render()
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''显示单个主题及其所有的条目'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  #  date_added 前面的减号指定按降序排列,即先显示最近的条目
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

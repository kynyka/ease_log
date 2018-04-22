# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect #这个URL模式将请求交给视图函数new_topic,接下来我们将编写这个函数。
from django.core.urlresolvers import reverse

from .models import Topic  # 首先导入与所需数据相关联的模型
from .forms import TopicForm

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

def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # 函数reverse()根据指定的URL模型确定URL,这意味着Django将在页面被请求时生成URL

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


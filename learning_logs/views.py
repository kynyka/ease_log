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
    topics = Topics.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

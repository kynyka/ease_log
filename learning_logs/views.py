# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404  # 用户提交主题后我们将使用这个类将用户重定向到网页 topics
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required  # Django提供了装饰器@login_required,让你能够轻松地实现这样的目标: 对于某些页面,只允许已登录的用户访问它们

from .models import Topic, Entry  # 首先导入与所需数据相关联的模型
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/index.html')  # 第1个实参为原始请求对象,第2个实参为可用于创建网页的模板

@login_required  # 让Python在运行topics()的代码前先运行login_required()的代码。login_required()的代码检查用户是否已登录，仅当用户已登录时，Django才运行topics()的代码。
# 如果用户未登录，就重定向到登录页面。[此部分工作在learning_logs/settings.py文件末尾行设置]
def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # 用户登录后,request对象将有一个user属性,这个属性存储了有关该用户的信息。
    context = {'topics': topics}  # 我们定义了一个将要发送给模板的上下文。上下文是一个字典，其中的键是我们将在模板中用来访问数据的名称，而值是我们要发送给模板的数据。在这里，只有一个键—值对，它包含我们将在网页中显示的一组主题。创建使用数据的网页时，除对象 request 和模板的路径外，我们还将变量 context 传递给 render()
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''显示单个主题及其所有的条目'''
    topic = get_object_or_404(Topic, id=topic_id) # 据L.4替换Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('-date_added')  #  date_added 前面的减号指定按降序排列,即先显示最近的条目
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user  # 将新主题的owner属性设置为当前用户
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # 函数reverse()根据指定的URL模型确定URL,这意味着Django将在页面被请求时生成URL

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''在特定的主题中添加新条目'''
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST) # 创建一个EntryForm实例,使用request对象中的POST数据来填充它
        if form.is_valid():
            new_entry = form.save(commit=False) # 实参commit=False,让Django创建一个新的条目对象,并将其存储到new_entry中,但不将它保存到数据库中
            new_entry.topic = topic # 将new_entry的属性topic设置为在这个函数开头从数据库中获取的主题
            new_entry.save() # 调用save()且不指定任何实参,这将把条目保存到数据库,并将其与正确的主题相关联
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))  # 将用户重定向到显示相关主题的页面。调用reverse()时,需要提供两个实参：要根据它来生成URL的URL模式的名称;列表 args,其中包含要包含在URL中的所有实参。在这里,列表args只有一个元素————topic_id。接下来,调用HttpResponseRedirect()将用户重定向到显示新增条目所属主题的页面,用户将在该页面的条目列表中看到新添加的条目。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''编辑既有条目'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求,使用当前条目填充表单
        form = EntryForm(instance=entry)  # 在请求方法为GET时,将执行if代码块;用实参instance=entry创建一个EntryForm实例。这个实参让Ejango创建一个表单,并使用既有条目对象中的信息填充它。用户将看到既有的数据,并能够编辑它们。
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(instance=entry, data=request.POST) # 处理POST请求时传递实参instance=entry和data=request.POST,让Django根据既有条目对象创建一个表单实例,并根据request.POST中的相关数据对其进行修改
        if form.is_valid(): # 然后我们检查表单是否有效,如果有效,就调用save(),且不指定任何实参
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id])) # 重定向到现显示条目所属主题的页面,用户将在其中看到编辑后的新版本条目

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def check_topic_owner(topic, request):
    if topic.owner != request.user:  # 禁止用户通过输入类似于前面的特定URL来访问其他用户的条目
        raise Http404
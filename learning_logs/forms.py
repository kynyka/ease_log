# -*- coding: utf-8 -*-
from django import forms

from .models import Topic

class TopicForm(forms.modelForm):  # 定义了一个名为TopicForm的类,它继承了forms.ModelForm
    class Meta:  # 最简单的ModelForm版本只包含一个内嵌的Meta类,它告诉Django根据哪个模型创建表单,以及在表单中包含哪些字段。
        model = Topic  # 根据模型Topic创建一个表单
        fields = ['text']  # 该表单只包含字段text
        labels = {'text': ''}  # 让Django不要为字段text生成标签

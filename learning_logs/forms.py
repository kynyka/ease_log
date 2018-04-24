# -*- coding: utf-8 -*-
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):  # 定义了一个名为TopicForm的类,它继承了forms.ModelForm
    class Meta:  # 最简单的ModelForm版本只包含一个内嵌的Meta类,它告诉Django根据哪个模型创建表单,以及在表单中包含哪些字段。
        model = Topic  # 根据模型Topic创建一个表单
        fields = ['text']  # 该表单只包含字段text
        labels = {'text': ''}  # 让Django不要为字段text生成标签,即input框前没字

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # widget是一个HTML表单元素,如单行文本框、多行文本区域或下拉列表。通过设置属性widgets,可覆盖Django选择的默认小部件。通过让Django使用 forms.Textarea,我们定制了字段'text'的输入小部件,将文本区域的宽度设置为80列,而不是默认的40列。

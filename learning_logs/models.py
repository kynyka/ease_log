# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User  # 首先导入django.contrib.auth中的模型User

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)  # charfield必须告知django该在数据库中预留多少空间
    date_added = models.DateTimeField(auto_now_add=True)  # 自动设置成当前日期和时间;见官网: ... ref/models/fields/
    owner = models.ForeignKey(User)  # 然后在Topic中添加字段owner,它建立到模型User的外键关系

    def __unicode__(self):  # Py 3.X用__str__()
        '''返回模型的字符串表示'''
        if len(self.text) > 50:
            return self.text + ' >w<'
        else:
            return self.text

class Entry(models.Model):  # 同Topic一样,继承Django基类Model
    '''学到的有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic)  # 第一个属性topic是一个ForeignKey实例
    text = models.TextField()  # text属性是TextField实例。这种字段不需要长度限制
    date_added = models.DateTimeField(auto_now_add=True)  # 这个属性让我们能够按创建顺序呈现条目，并在每个条目旁边放置时间戳

    class Meta:  # 在类中嵌套了Meta类。Meta存储用于管理模型的额外信息,在这里它让我们能够设置一个特殊属性,让Django在需要时使用Entries来表示多个条目。如果没有这个类,Django将使用Entrys来表示多个条目。
        verbose_name_plural = 'entries'

    def __unicode__(self):  # 告诉Django呈现条目时应显示哪些信息
        '''返回模型的字符串表示'''
        return self.text[:50] + '...'

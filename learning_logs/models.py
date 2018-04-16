# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)  # charfield必须告知django该在数据库中预留多少空间
    date_added = models.DateTimeField(auto_now_add=True)  # 自动设置成当前日期和时间;见官网: ... ref/models/fields/

    def __unicode__(self):  # Py 3.X用__str__()
        '''返回模型的字符串表示'''
        return self.text

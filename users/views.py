# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout  # ㈠ 从django.contrib.auth中导入了函数logout()

# Create your views here.
def logout_view(request):
    # 函数 logout_view() 很简单：只是导入Django函数 logout() ，并调用它，再重定向到主页。
    '''註銷用戶'''
    logout(request)  # ㈡ 调用函数logout(),它要求将request对象作为实参
    return HttpResponseRedirect(reverse('learning_logs:index'))  # ㈢ 重定向到主页

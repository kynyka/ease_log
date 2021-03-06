# -*- coding: utf-8 -*-
"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace='users')),  #任何以单词users打头的URL（如http://localhost:8000/users/login/）都能匹配。创建命名空间'users',以便将应用程序 learning_logs 的URL同应用程序 users 的URL区分开来
    url(r'', include('learning_logs.urls', namespace='learning_logs')),  # 实参namespace让我们能够将learning_logs的URL同项目中的其他URL区分开来
]

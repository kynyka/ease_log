# -*- coding: utf-8 -*-
"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@*c@tv41$1+$f8_zvc#1mzm7^o!hsn#2!i*0rns$w#^-6&581s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # 查看本地自定义的404/500页面时,L.27为False,L.29为['localhost']


# Application definition

INSTALLED_APPS = [  # 它告诉Django项目是由哪些应用程序组成的
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 第三方应用程序
    'bootstrap3',

    # 我的应用程序
    'learning_logs',  # 即python manage.py startapp xxx 时创建的那个名字
    'users',  # 创建的这个应用程序,包含并处理用户账户相关的所有功能
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learning_log.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'learning_log/templates')], # 让Django在根模板目录中查找错误页面模板
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_log.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 我的设置
LOGIN_URL = '/users/login/'

# django-bootstrap3的设置[让django-bootstrap3包含jQuery]
BOOTSTRAP3 = {
    'include_jquery': True,
}

# Heroku设置
'''os.getcwd()获取当前的工作目录（当前运行的文件所在的目录）。在Heroku部署中，这个目录总是/app。在本地部署中，这个目录通常是项目文件夹的名称（就本项目而言，为learning_log）。这个 if 测试确保仅当项目被部署到Heroku时，才运行这个代码块。这种结构让我们能够将同一个设置文件用于本地开发环境和在线服务器。'''
cwd = os.getcwd()
if cwd == '/app' or cwd[:4] == '/tmp': # 更新：https://ehmatthes.github.io/pcc/chapter_20/README.html#updates
    import dj_database_url # 导入dj_database_url，用于在Heroku上配置服务器。Heroku使用PostgreSQL(也叫Postgres)————一种比SQLite更高级的数据库
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost')
    }

    # 让request.is_secure()承认X-Forwarded-Proto头 [i.e.支持HTTPS请求]
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # 支持所有的主机头（host header）[i.e.让Django能够使用Heroku的URL来提供项目提供的服务]
    # 将['*']改为['logease.herokuapp.com'], 只允许Heroku托管这个项目
    ALLOWED_HOSTS = ['logease.herokuapp.com']

    # 让Django不在错误发生时显示敏感信息; 注意本地仍能看到调试信息(L.27),因为现在这块儿代码只对部署的环境有作用
    DEBUG = False

    # 静态资产配置 [i.e.设置项目，使其能够在Heroku上正确地提供静态文件]
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
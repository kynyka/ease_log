# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate  # ㈠ 从django.contrib.auth中导入了函数logout()
from django.contrib.auth.forms import UserCreationForm  # 导入默认表单

# Create your views here.
def logout_view(request):
    # 函数 logout_view() 很简单：只是导入Django函数 logout() ，并调用它，再重定向到主页。
    '''註銷用戶'''
    logout(request)  # ㈡ 调用函数logout(),它要求将request对象作为实参
    return HttpResponseRedirect(reverse('learning_logs:index'))  # ㈢ 重定向到主页

def register(request):
    # 在注册页面首次被请求时,视图函数register()需要显示一个空的注册表单,并在用户提交填写好的注册表单时对其进行处理。如果注册成功,这个函数还需让用户自动登录。
    '''注册新用户'''
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()  # 如果提交的数据有效,就调用表单的方法save()将用户名和密码的散列值保存到数据库中。方法save()返回新创建的用户对象,我们将其存储在new_user中
            # 让用户自动登录,再重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])  # 保存用户的信息后,我们让用户自动登录,这包含两个步骤。首先,调用authenticate(),并将实参new_user.username和密码传递给它。用户注册时被要求输入密码两次: 由于表单是有效的,我们知道输入的这两个密码是相同的,因此可以使用其中任何一个。在这里,我们从表单的POST数据中获取与键'password1'相关联的值。如果用户名和密码无误,方法authenticate()将返回一个通过了身份验证的用户对象,而我们将其存储在authenticated_user中
            login(request, authenticated_user)  # 接下来,我们调用函数login(),并将对象request和authenticated_user传递给它,这将为新用户创建有效的会话。
            return HttpResponseRedirect(reverse('learning_logs:index'))  # 最后,我们将用户重定向到主页,其页眉中显示了一条个性化的问候语,让用户知道注册成功了

    context = {'form': form}
    return render(request, 'users/register.html', context)

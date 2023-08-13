import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from classbehavior import models
from classbehavior import tools
from classbehavior.models import user

import torch
import cv2



def index(request):
    if request.session.get('login.html') == None:
        return redirect('/login')
    return render(request, 'index.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    item_list = models.user.objects.all()
    for objects in item_list:
        if objects.username == username and objects.password == password:
            request.session['login.html'] = True
            return redirect('/index')
    return render(request, 'login.html', {"mess": "用户名或密码输入错误"})


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')
    email = request.POST.get('email')
    if password != password1:
        return render(request, 'register.html', {"mess": '两次密码输入不同，请重新输入！'})
    if len(password) <= 7:
        return render(request, 'register.html', {"mess": '密码长度至少8位！'})
    data_list = models.user.objects.all()
    for data in data_list:
        if username == data.username:
            return render(request, 'register.html', {"mess": '该用户名已存在，请重新输入！'})
    for data in data_list:
        if email == data.email:
            return render(request, 'register.html', {"mess": '此邮箱已被使用，请重新输入！'})
    user.objects.create(username=username, password=password, email=email)
    return render(request, 'login.html', {"mess": '注册成功！请登录'})

def logout(request):
    request.session.flush() #清空session
    return redirect('/login')


def head(request):
    return render(request, 'head.html')

def shibie(request):
    return render(request, 'shibie.html')


def baogao(request):
    return render(request, 'baogao.html')


def help(request):
    return render(request, 'help.html')


def settings(request):
    return render(request, 'settings.html')




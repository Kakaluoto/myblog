# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Post, Product, Mood
from datetime import datetime
import random


# Create your views here.
def showArticle(request, pid=None, del_pass=None):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    now = datetime.now()
    try:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
    except:
        user_id = None
        message = '如果要张贴信息，那么每个字段都要填写...'

    if del_pass and pid:
        try:
            post = Post.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "数据删除成功"
            else:
                message = "密码错误"
    elif user_id != None:
        mood = Mood.objects.get(status=user_mood)
        post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功保存！请记得你的编辑密码【{}】!，信息需经审查后才会显示。'.format(user_pass)
    return render(request, 'index.html', locals())


def homepage(request):
    return render(request, 'menu.html')


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def about(request):
    quotes = [
        '知识不求人。',
        '己所不欲，勿施于人。',
        '没有调查就没有发言权。',
        '我之所以想变强，是为了活得轻松写意。'
    ]
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())


def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())


def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    return render(request, 'disp.html', locals())


def verifier(request):
    username = request.POST.get('user_id', '')
    password = request.POST.get('user_pass', '')
    nextpage = request.POST.get('next_page', 'article')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/login/' + nextpage)
    else:
        return render(request, 'error.html', {'message': '用户名或密码不正确'})


def mylogin(request, id):
    return render(request, 'login.html', locals())

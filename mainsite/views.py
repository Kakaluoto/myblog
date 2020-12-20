# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from .models import Post, Product
from datetime import datetime
import random


# Create your views here.
def showArticle(request):
    posts = Post.objects.all()
    now = datetime.now()
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

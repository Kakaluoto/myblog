# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from .models import Post, Product
from datetime import datetime


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')


def about(request):
    return render(request, 'about.html')


def listing(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='uft-8'>
        <title>
            货物列表
        </title>
    </head>
    <body>
        <h2>当前存货列表</h2>
        <hr>
        <table width=400 border=1 bgcolor='#ccffcc'>
        {}
        </table>
    </body>
    </html>
    '''
    products = Product.objects.all()
    tags = '<tr><td>产品</td><td>售价</td><td>库存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.restp)
    return HttpResponse(html.format(tags))


def disp_detail(request, sku):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='uft-8'>
        <title>{}</title>
    </head>
    <body>
        <h2>{}</h2>
        <hr>
        <table width=400 border=1 bgcolor='#ccffcc'>
        {}
        </table>
        <a href='/list'>返回列表</a>
    </body>
    </html>
    '''
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    tags = '<tr><td>产品编号</td><td>{}</td></tr>'.format(p.sku)
    tags = tags + '<tr><td>产品名称</td><td>{}</td></tr>'.format(p.name)
    tags = tags + '<tr><td>库存数量</td><td>{}</td></tr>'.format(p.restp)
    return HttpResponse(html.format(p.name, p.name, tags))

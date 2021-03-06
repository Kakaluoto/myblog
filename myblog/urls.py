"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainsite.views import showpost, homepage, about, listing, disp_detail, showArticle, verifier, mylogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('article/', showArticle, name='article'),
    path('article/<int:pid>/<str:del_pass>', showArticle),
    path('post/<slug:slug>', showpost),
    path('about/', about),
    path('list/', listing),
    path('login/<str:id>', mylogin),
    path('verify/', verifier, name='verifier'),  # ��Ⱦ��¼����
    path('list/<str:sku>/', disp_detail),
]

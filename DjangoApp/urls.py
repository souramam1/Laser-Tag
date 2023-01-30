"""DjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http.response import HttpResponse, Http404, HttpResponseNotFound, Http404
from django.urls import path,include,reverse
from django.shortcuts import render


def home_view(request):
    #return HttpResponse("HOME PAGE")
    return render(request,'welcome_page/base.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome_page/',include('welcome_page.urls')),
    path('',home_view,name = 'home')
]

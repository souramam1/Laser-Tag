from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.
def simple_view(request):
    #return HttpResponse('HELLO') 
    return render(request, 'welcome_page/base.html')  # .html

def about_view(request):
    return render(request, 'welcome_page/about.html') 

def software_view(request):
    return render(request, 'welcome_page/software.html')

def contact_view(request):
    return render(request, 'welcome_page/contact.html')



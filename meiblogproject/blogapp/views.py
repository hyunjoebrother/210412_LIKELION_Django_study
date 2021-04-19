from django.shortcuts import render

# model을 화면에 출력하기 위해 views.py에 import
from .models import Blog

# Create your views here.
def home(request) :
    blogs = Blog.objects # model로부터 객체 목록을 전달
    return render(request, 'home.html', {'blogs' : blogs})

# 이제 APP 폴더 내에 templates 폴더 내에 home.html 작업
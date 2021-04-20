from django.shortcuts import render, get_object_or_404

# model을 화면에 출력하기 위해 views.py에 import
from .models import Blog

# Create your views here.
def home(request) :
    blogs = Blog.objects # model로부터 객체 목록을 전달
    return render(request, 'home.html', {'blogs' : blogs})

# 이제 APP 폴더 내에 templates 폴더 내에 home.html 작업


# detail 함수를 만들자 - 몇 번 객체를 다룰지에 따라 다름
def detail(request, blog_id) :
    # 특정 번호의 객체를 담기 위해 검색조건 pk 지정
    # 다음 함수로 object를 get하기도 하고 404 예외처리도 가능 + import하자
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog' : blog_detail})

# 이제 detail.html 작업하자 
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request) :
    blogs = Blog.objects # 클래스.objects : model로부터 객체 목록(Queryset)을 전달받음
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id) :
    # 몇 번 객체를 다룰 것인지에 대한 인자 blog_id
    # 이용자가 원한 몇 번 블로그 객체를 사용하도록하는 함수 + import 고고
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog' : blog_detail})

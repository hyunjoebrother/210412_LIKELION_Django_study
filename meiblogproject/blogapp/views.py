from django.shortcuts import render, get_object_or_404, redirect

# model을 화면에 출력하기 위해 views.py에 import
from .models import Blog

from django.utils import timezone


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

# Create 작업 시작 - 글쓰기 페이지 만들기
def new(request) : # new.html 화면 띄워줌
    return render(request, 'new.html')

# create 함수 실행을 위한 url 연결
def create(request) : # 입력값을 DB에 넣어주는 함수, html X
    # Blog 클래스로부터 create_blog라는 객체 생성
    create_blog = Blog()

    # new.html에서 입력값을 가져옴 GET
    create_blog.title = request.GET['title']
    create_blog.pub_date = timezone.datetime.now() # import 필요
    create_blog.body = request.GET['body']

    # Query Method - 객체들을 DB에 저장
    create_blog.save()

    # 글 생성 후 url 바로 이동
    return redirect('/detail/' + str(create_blog.id))

# Update 작업 시작
def edit(request, edit_id) :
    # get 함수로 edit_id를 받아서 edit_blog 에 담고 전달
    edit_blog = Blog.objects.get(id = edit_id)

    return render(request, 'edit.html', {'blog' : edit_blog})

def update(request, update_id) : # 글 edit하여 덮여쓰고 제출
    update_blog = Blog.objects.get(id = update_id)
    
    update_blog.title = request.GET['title']
    update_blog.pub_date = timezone.datetime.now() # import 필요
    update_blog.body = request.GET['body']

    # Query Method - 객체들을 DB에 저장
    update_blog.save()

    # 글 생성 후 url 바로 이동
    return redirect('/detail/' + str(update_blog.id))

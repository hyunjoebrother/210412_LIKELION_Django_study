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


## CRUD 작업 시작

# new 함수 : new.html을 띄워주는 함수
def new(request) :
    return render(request, 'new.html')

# html 파일 필요 없음 ㅇㅇ create 함수 실행을 위한 url 연결임. 이제 작업하자
# create 함수 : 입력받은 내용을 DB에 넣어주는 함수
def create(request) :
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()


    return render(request, 'create.html')
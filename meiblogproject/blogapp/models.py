from django.db import models

# Create your models here.
# App 폴더 등록하고 class 만들자
class Blog(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    # 작업 후 DB에 알려주는 migration 작업 ON
    # ROCKET 확인 후 ADMIN 계정 만들고 
    # admin.py에 import Blog

    # 제목을 title로 띄우기 위해서 함수 등록
    def __str__(self) :
        return self.title

    # 이제 model을 화면에 출력하기 위해 views.py에 import
#### URL 효율적 관리를 위해 APP폴더에 새로 만든 파일
# 각 APP 폴더 안에 각 App의 URL을 넣어보자

from django.contrib import admin
from django.urls import path

# import blogapp.views
from . import views

urlpatterns = [
    ## detail/~ url 임 ㅇㅇ

    # Read 작업
    path('<int:blog_id>', views.detail, name = 'detail'),
    # Create 작업
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'), # 연결용임 html 없음
    # Update 작업
    path('edit/<int:edit_id>', views.edit, name = 'edit'),
    path('update/<int:update_id>', views.update, name = 'update'),

]
"""myblogproject URL Configuration

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
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = 'home'),
    path('blog/<int:blog_id>', blog.views.detail, name = 'detail'),

    # CRUD 시작
    path('blog/new/', blog.views.new, name = 'new'),
    path('blog/create', blog.views.create, name = 'create'), # create 함수 연결용임 html 파일 필요없음
    path('blog/edit/<int:edit_id>', blog.views.edit, name = 'edit'),
    path('blog/update/<int:update_id>', blog.views.update, name = 'update'),
    path('blog/delete/<int:delete_id>', blog.views.delete, name = 'delete'),
]

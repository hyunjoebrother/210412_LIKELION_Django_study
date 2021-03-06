"""mymeiblogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = 'home'),

    # detail할 때 url부터 작업 시작
    # path converter로 type 지정해줌 -> home.html에서 url 태그 수정
    #path('detail/<int:blog_id>', blogapp.views.detail, name = 'detail'),
    path('detail/', include('blogapp.urls')), # URL 정리!
]

"""BBS3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from BBS3.settings import MEDIA_ROOT
from django.views.static import serve
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    re_path('^$', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('get_code', views.get_code, name='get_code'),
    path('logout', views.logout, name='logout'),
    path('set_password', views.set_password, name='set_password'),
    path('set_avatar', views.set_avatar, name='set_avatar'),
    path('up_or_down', views.up_or_down, name='up_or_down'),
    path('comment', views.comment, name='comment'),
    path('backend/', views.base, name='backend'),
    path('backend/', include([
        path('base', views.base, name='base'),
        path('add/article', views.add_article, name='add_article'),
        path('del/article', views.del_article, name='del_article'),
        path('edit/article<int:article_id>', views.edit_article, name='edit_article'),
    ])),
    path('upload_json', views.upload_json, name='upload_json'),

    re_path(r'^(?P<username>\w+)/$', views.site, name='site'),
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/', views.article_detail, name='article_detail'),
    re_path(r'^(?P<username>\w+)/article/(?P<condition>category|tag|date)/(?P<param>.*)/', views.site, name='site'),

]
















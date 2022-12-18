from django.shortcuts import render, HttpResponse, redirect, reverse
from app01.forms.regform import RegForm
from app01.forms.loginform import LoginForm
from django.contrib import auth
from app01 import models
from django.http import JsonResponse
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.db.models import F
import json
from django.db import transaction
from BBS3.settings import MEDIA_ROOT
import os
from uuid import uuid1
from bs4 import BeautifulSoup
from utils.mypage import Pagination


def home(request):
    article_queryset = models.Article.objects.all()
    return render(request, 'home.html', locals())


def register(request):
    form_obj = RegForm()
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 2000, 'url': '', 'msg': ''}
            form_obj = RegForm(request.POST)
            if form_obj.is_valid():
                form_data = form_obj.cleaned_data
                form_data.pop('confirm_password')
                avatar = request.FILES.get('avatar')
                if avatar:
                    form_data['avatar'] = avatar
                models.UserInfo.objects.create_user(**form_data)
                back_dic['url'] = reverse('login')
            else:
                back_dic['code'] = 4000
                back_dic['msg'] = form_obj.errors
            return JsonResponse(back_dic)
    return render(request, 'register.html', locals())


def login(request):
    form_obj = LoginForm()
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 2000, 'url': '', 'msg': ''}
            form_obj = LoginForm(request.POST)
            if form_obj.is_valid():
                form_data = form_obj.cleaned_data
                code = request.POST.getlist('code')[0]
                if code == request.session.get('code'):
                    user_obj = models.UserInfo.objects.filter(username=form_data.get('username')).first()
                    auth.login(request, user_obj)
                    back_dic['url'] = reverse('home')
                else:
                    back_dic['code'] = 4001
                    back_dic['msg'] = '验证码错误'
            else:
                back_dic['code'] = 4000
                back_dic['msg'] = form_obj.errors
            return JsonResponse(back_dic)
    return render(request, 'login.html', locals())


def get_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_code(request):
    img_obj = Image.new('RGB', (360, 35), get_color())
    img_draw = ImageDraw.Draw(img_obj)
    img_font = ImageFont.truetype(
        'static/font/Rondal-Semibold.ttf', size=24,
    )
    code = ''
    for i in range(4):
        str_lower = string.ascii_lowercase
        str_upper = string.ascii_uppercase
        str_digit = string.digits
        temp = random.choice(random.choice([str_lower, str_upper, str_digit]))
        img_draw.text((i * 45 + 60, 0), temp, get_color(), img_font)
        code += temp
    print(code)
    request.session['code'] = code
    io_obj = BytesIO()
    img_obj.save(io_obj, 'PNG')
    return HttpResponse(io_obj.getvalue())


def logout(request):
    auth.logout(request)
    return redirect('home')


def set_password(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 2000, 'url': '', 'msg': ''}
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                if old_password == new_password:
                    back_dic['code'] = 4000
                    back_dic['msg'] = '新密码不能和旧密码相同'
                else:
                    is_right = request.user.check_password(old_password)
                    if is_right:
                        request.user.set_password(new_password)
                        request.user.save()
                        back_dic['url'] = reverse('login')
                    else:
                        back_dic['code'] = 4000
                        back_dic['msg'] = '旧密码错误'
            else:
                back_dic['code'] = 4000
                back_dic['msg'] = '确认密码错误'
            return JsonResponse(back_dic)
    return render(request, 'errors.html')


def set_avatar(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 2000, 'url': reverse('home'), 'msg': ''}
            avatar = request.FILES.get('avatar')
            try:
                request.user.avatar = avatar
                request.user.save()
            except:
                back_dic['code'] = 4000
                back_dic['msg'] = '服务器错误'
            return JsonResponse(back_dic)
    return render(request, 'errors.html')


def site(request, username, **kwargs):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        return render(request, 'errors.html')
    blog = user_obj.blog
    article_queryset = models.Article.objects.filter(blog=blog)
    if kwargs:
        condition = kwargs.get('condition')
        param = kwargs.get('param')
        if condition == 'category':
            article_queryset = article_queryset.filter(category_id=param)
        elif condition == 'tag':
            article_queryset = article_queryset.filter(tags__id=param)
        else:
            try:
                year, month = param.split('-')
                article_queryset = article_queryset.filter(create_time__month=month)
                print(article_queryset)
                if not article_queryset:
                    return render(request, 'errors.html')
            except:
                return render(request, 'errors.html')
    return render(request, 'site.html', locals())


def article_detail(request, username, article_id):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        return render(request, 'errors.html')
    blog = user_obj.blog
    article_obj = models.Article.objects.filter(blog=blog, pk=article_id).first()
    comment_queryset = models.Comment.objects.filter(article=article_obj)
    return render(request, 'article_detail.html', locals())


def up_or_down(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 2000, 'msg': ''}
            is_up = request.POST.get('is_up')
            article_id = request.POST.get('article_id')
            is_up = json.loads(is_up)
            try:
                with transaction.atomic():
                    # 是否是自己的文章
                    user_obj = models.Article.objects.filter(pk=article_id).first().blog.userinfo
                    if not user_obj == request.user:
                        # 是否已经支持过
                        if not models.UpAndDown.objects.filter(user_id=request.user.id, article_id=article_id):
                            # 赞或踩
                            if is_up:
                                models.Article.objects.filter(pk=article_id).update(up_num=F('up_num') + 1)
                                back_dic['msg'] = '点赞成功'
                            else:
                                models.Article.objects.filter(pk=article_id).update(down_num=F('down_num') + 1)
                                back_dic['msg'] = '点踩成功'
                            models.UpAndDown.objects.filter(article_id=article_id).create(is_up=is_up,
                                                                                          user=request.user,
                                                                                          article_id=article_id)
                        else:
                            back_dic['code'] = 4000
                            back_dic['msg'] = '您已支持过'
                    else:
                        back_dic['code'] = 4000
                        back_dic['msg'] = '不能对自己的文章进行点赞点踩'
            except:
                back_dic['code'] = 4000
                back_dic['msg'] = '服务器错误'
            return JsonResponse(back_dic)
    return render(request, 'errors.html')


def comment(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 2000, 'msg': ''}
            content = request.POST.get('content')
            article_id = request.POST.get('article_id')
            username = request.POST.get('username')
            user_obj = models.UserInfo.objects.filter(username=username).first()
            user = request.user
            parent_id = request.POST.get('parent_id')
            try:
                if parent_id:
                    models.Comment.objects.create(article_id=article_id, user=user, content=content,
                                                  parent_id=parent_id)
                else:
                    models.Comment.objects.create(article_id=article_id, user=user, content=content)
                models.Article.objects.filter(pk=article_id, blog__userinfo=user_obj).update(
                    comment_num=F('comment_num') + 1)
                back_dic['msg'] = '评论成功'
            except:
                back_dic['code'] = 4000
                back_dic['msg'] = '服务器错误'
            finally:
                return JsonResponse(back_dic)
    return render(request, 'errors.html')


def base(request):
    user_obj = request.user
    article_queryset = models.Article.objects.filter(blog__userinfo=user_obj).all().order_by('-create_time')

    current_page = request.GET.get('page', 1)
    all_count = article_queryset.count()
    page_obj = Pagination(current_page, all_count, 3)
    page_queryset = article_queryset[page_obj.start:page_obj.end]
    return render(request, 'backend/base.html', locals())


def add_article(request):
    article_obj = models.Article.objects.filter(blog=request.user.blog).first()
    category_list = models.Category.objects.filter(blog__userinfo=request.user)
    tag_list = models.Tag.objects.filter(blog__userinfo=request.user)
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            category = request.POST.get('category')
            tag_list = request.POST.getlist('tags')
            soup = BeautifulSoup(content, 'lxml')
            tags = soup.find_all()
            for tag in tags:
                if tag.name == 'script':
                    tag.decompose()
            content = soup.text
            desc = content[:150]
            new_article_obj = models.Article.objects.create(
                 blog=request.user.blog, title=title, content=str(soup), desc=desc, category_id=category
            )
            lst = []
            for i in tag_list:
                lst.append(models.ArticleToTag(article=new_article_obj, tag_id=i))
            models.ArticleToTag.objects.filter(article=article_obj).bulk_create(lst)
            return redirect('base')
        except:
            return HttpResponse('500 error')
    return render(request, 'backend/add_article.html', locals())


def del_article(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'msg': ''}
            article_id = request.POST.get('article_id')
            try:
                models.Article.objects.filter(pk=article_id).delete()
                back_dic['msg'] = '删除成功'
            except Exception as e:
                back_dic['msg'] = '删除失败'
            finally:
                return JsonResponse(back_dic)
    return render(request, 'errors.html')


def edit_article(request, article_id):
    article_obj = models.Article.objects.filter(pk=article_id).first()
    category_list = models.Category.objects.filter(blog=request.user.blog)
    tag_list = models.Tag.objects.filter(blog=request.user.blog)
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            category = request.POST.get('category')
            tag_list = request.POST.getlist('tags')
            soup = BeautifulSoup(content, 'lxml')
            tags = soup.find_all()
            for tag in tags:
                if tag.name == 'script':
                    tag.decompose()
            content = soup.text
            desc = content[:150]
            with transaction.atomic():
                models.Article.objects.filter(pk=article_id).update(
                    title=title, content=str(soup), desc=desc, category_id=category
                )
                models.ArticleToTag.objects.filter(article_id=article_id).delete()
                lst = []
                for j in tag_list:
                    lst.append(models.ArticleToTag(article=article_obj, tag_id=j))
                models.ArticleToTag.objects.filter(article=article_obj).bulk_create(lst)
            return redirect('base')
        except:
            return HttpResponse('500 error')
    return render(request, 'backend/edit_article.html', locals())


def upload_json(request):
    """
    //成功时
    {
            "error" : 0,
            "url" : "http://www.example.com/path/to/file.ext"
    }
    //失败时
    {
            "error" : 1,
            "message" : "错误信息"
    }
    :param request:
    :return:
    """
    if request.method == 'POST':
        back_dic = {'url': '', 'error': 0, 'message': ''}
        try:
            file_path = os.path.join(MEDIA_ROOT, 'upload_img')
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            file_obj = request.FILES.get('imgFile')
            file_name = str(uuid1()) + file_obj.name
            path = os.path.join(file_path, file_name)
            with open(path, 'wb') as f:
                for line in file_obj:
                    f.write(line)
            back_dic['url'] = '/media/upload_img/%s' % file_name
        except:
            back_dic['error'] = 1
            back_dic['message'] = '上传失败'
        return JsonResponse(back_dic)
    return render(request, 'errors.html')

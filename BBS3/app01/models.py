from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.BigIntegerField(verbose_name='手机号', null=True, blank=True)
    avatar = models.FileField(verbose_name='用户头像', upload_to='avatar/', default='/static/img/default.jpg')
    create_time = models.DateTimeField(verbose_name='用户创建时间', auto_now_add=True)
    gender_choice = (
        (1, '男'),
        (2, '女'),
        (3, '未知'),
    )
    gender = models.IntegerField(verbose_name='用户性别', choices=gender_choice, default=3)
    desc = models.CharField(verbose_name='个人简介', max_length=128, null=True, blank=True)

    blog = models.OneToOneField(to='Blog', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username


class Blog(models.Model):
    site_name = models.CharField(verbose_name='站点名称', max_length=64)
    site_title = models.CharField(verbose_name='站点标题', max_length=64, null=True, blank=True)
    site_css = models.CharField(verbose_name='站点样式', max_length=64, null=True, blank=True)

    class Meta:
        verbose_name_plural = '个人站点表'

    def __str__(self):
        return self.site_name


class Category(models.Model):
    name = models.CharField(verbose_name='文章分类', max_length=64)
    blog = models.ForeignKey(to='Blog', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = '文章分类表'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='文章分类', max_length=64)
    blog = models.ForeignKey(to='Blog', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = '文章标签表'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=64)
    desc = models.CharField(verbose_name='文章简介', max_length=255)
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateTimeField(verbose_name='文章创建时间', auto_now_add=True)

    up_num = models.IntegerField(verbose_name='点赞数', default=0)
    down_num = models.IntegerField(verbose_name='点踩数', default=0)
    comment_num = models.IntegerField(verbose_name='评论数', default=0)

    blog = models.ForeignKey(to='Blog', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(
        to='Tag',
        through='ArticleToTag',
        through_fields=('article', 'tag')
    )

    class Meta:
        verbose_name_plural = '文章表'

    def __str__(self):
        return self.title


class ArticleToTag(models.Model):
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '文章标签表'

    def __str__(self):
        return self.article.title


class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    is_up = models.BooleanField(verbose_name='是否点赞', null=True, blank=True)

    class Meta:
        verbose_name_plural = '点赞点踩表'


class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)

    parent = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '评论表'


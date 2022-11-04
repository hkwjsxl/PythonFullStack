from django import template
from app01 import models
from django.db.models import Count
from django.db.models.functions import TruncMonth


register = template.Library()


@register.inclusion_tag(filename='left_tag.html')
def left_tag(username):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog
    article_queryset = models.Article.objects.filter(blog=blog)
    category_queryset = models.Category.objects.filter(blog=blog) \
        .annotate(count_num=Count('article__pk')).values('name', 'count_num', 'pk')
    tag_queryset = models.Tag.objects.filter(blog=blog) \
        .annotate(count_num=Count('article__pk')).values('name', 'count_num', 'pk')
    date_queryset = models.Article.objects.filter(blog=blog) \
        .annotate(month=TruncMonth('create_time')).order_by('-month').values('month') \
        .annotate(count_num=Count('pk')).values('month', 'count_num')
    return locals()



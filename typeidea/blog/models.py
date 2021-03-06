from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField('名称', max_length=10)
    status = models.IntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    is_nav = models.BooleanField('是否为导航', default=False)
    owner = models.ForeignKey(User, verbose_name='创建者')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField('名称', max_length=10)
    status = models.IntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    owner = models.ForeignKey(User, verbose_name='创建者')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField('标题', max_length=20)
    desc = models.CharField('摘要', max_length=200)
    content = models.TextField('内容', help_text='正文必须为MarkDown格式')
    status = models.IntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    category = models.ForeignKey(Category, verbose_name='范围')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title















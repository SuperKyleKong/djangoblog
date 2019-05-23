from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField('标题', max_length=100)
    href = models.URLField(verbose_name='链接')
    status = models.IntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    weight = models.PositiveIntegerField('权重', choices=zip(range(1, 6), range(1, 6)),
                                         default=1, help_text='权重高展示顺序靠前')
    owner = models.ForeignKey(User, verbose_name='创建者')

    class Meta:
        verbose_name = verbose_name_plural = '友链'

    def __str__(self):
        return self.title


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField('标题', max_length=100)
    display_type = models.PositiveIntegerField('类型', choices=SIDE_TYPE, default=1)
    status = models.IntegerField('状态', choices=STATUS_ITEMS, default=STATUS_SHOW)
    content = models.CharField('内容', max_length=200, help_text='如果设置的不是HTML类型，可为空')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    owner = models.ForeignKey(User, verbose_name='创建者')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'

    def __str__(self):
        return self.title













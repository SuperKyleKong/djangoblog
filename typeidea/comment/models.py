from django.db import models
from blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    nickname = models.CharField('昵称', max_length=20)
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网站')
    content = models.CharField('内容', max_length=200)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    target = models.ForeignKey(Post, verbose_name='评论对象')

    class Meta:
        verbose_name = verbose_name_plural = '评论'

    def __str__(self):
        return self.nickname









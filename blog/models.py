from django.db import models

from agent.models import NULLABLE


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержание статьи')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='изображение')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

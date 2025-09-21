from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(max_length=1000, verbose_name='Контент', null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_indicator = models.BooleanField(default=True)
    views_counter = models.IntegerField(verbose_name='Счетчик просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['title']

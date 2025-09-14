from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории')
    description = models.TextField(max_length=250, verbose_name='Описание', null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='media/images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['created_at']
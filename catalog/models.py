from django.db import models


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
    name = models.CharField(
        unique=True,
        max_length=60,
        verbose_name='Имя',
        default='Unnamed',
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=250,
        verbose_name='Описание',
        blank=True,
        null=True,
        default='Unnamed'
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        blank=True,
        null=True
    )
    price = models.IntegerField(
        verbose_name='Цена',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения'
    )
    owner = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['created_at']
        permissions = [
            ('can_unpublish_products', 'Can unpublish products'),
        ]

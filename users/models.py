from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name='Name')
    email = models.EmailField(unique=True, max_length=50, verbose_name='Email')

    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=10, verbose_name='Телефон', blank=True, null=True,
                                    help_text='Введите номер телефона')
    country = models.CharField(max_length=20, verbose_name='Страна', blank=True, null=True, help_text='Откуда вы')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
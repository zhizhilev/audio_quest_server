from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    logo = models.ImageField(verbose_name='Логотип', null=True, blank=True)
    create_datetime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Дата изменения', blank=True, auto_now=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    address = models.TextField(verbose_name='Адрес', null=True, blank=True)


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
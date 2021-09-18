from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    desc = models.TextField(verbose_name='Описание', blank=True, default="")
    create_datetime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    image = models.ImageField(verbose_name='Файл', upload_to='uploads/%Y/%m/%d/', null=True, blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
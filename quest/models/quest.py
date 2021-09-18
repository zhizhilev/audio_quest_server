from django.db import models

class Quest(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='quests')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', blank=True)
    create_datetime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    category =  models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_quests')

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'
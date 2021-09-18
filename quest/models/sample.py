from django.db import models
import uuid

class Sample(models.Model):

    SEC_TO_ANSWER_DEFAULT = 3
    SEC_TO_END_DEFAULT = 0

    name = models.CharField(verbose_name='Название', max_length=200)
    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    create_datetime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    uid = models.UUIDField(verbose_name='Уникальный идентификатор', default=uuid.uuid4, editable=False, null=True, blank=True)
    is_main = models.BooleanField(verbose_name='Заглавный семпл квеста', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    quest = models.ForeignKey('Quest', verbose_name='Квест' , on_delete=models.CASCADE, related_name='samples')

    positive_answer = models.ForeignKey('self',verbose_name='Ответ Да', on_delete=models.CASCADE, null=True, blank=True, related_name='parent_sample_positive')
    negative_answer = models.ForeignKey('self',verbose_name='Ответ Нет', on_delete=models.CASCADE, null=True, blank=True, related_name='parent_sample_negative')
    no_answer = models.ForeignKey('self', verbose_name='Нет ответа', on_delete=models.CASCADE, null=True, blank=True, related_name='parent_sample_no_answer')
    sec_to_answer = models.IntegerField(verbose_name='Секунд на ответ', default=SEC_TO_ANSWER_DEFAULT, blank=True)
    sec_to_end = models.IntegerField(verbose_name='За сколько секунд до конца включать распознавалку(если длинные аудиофайлы с пустотой)', default=SEC_TO_END_DEFAULT, blank=True)

    class Meta:
        verbose_name = 'Семпл'
        verbose_name_plural = 'Семплы'
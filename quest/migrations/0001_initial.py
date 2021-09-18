# Generated by Django 3.2.6 on 2021-09-18 06:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Логотип')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('desc', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(blank=True, verbose_name='Опубликовано')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='quest.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_quests', to='quest.category')),
            ],
            options={
                'verbose_name': 'Квест',
                'verbose_name_plural': 'Квесты',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('uid', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, verbose_name='Уникальный идентификатор')),
                ('is_main', models.BooleanField(blank=True, null=True, verbose_name='Заглавный семпл квеста')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Файл')),
                ('sec_to_answer', models.IntegerField(blank=True, default=3, verbose_name='Секунд на ответ')),
                ('sec_to_end', models.IntegerField(blank=True, default=0, verbose_name='За сколько секунд до конца включать распознавалку(если длинные аудиофайлы с пустотой)')),
                ('negative_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_sample_negative', to='quest.sample', verbose_name='Ответ Нет')),
                ('no_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_sample_no_answer', to='quest.sample', verbose_name='Нет ответа')),
                ('positive_answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_sample_positive', to='quest.sample', verbose_name='Ответ Да')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='quest.quest', verbose_name='Квест')),
            ],
            options={
                'verbose_name': 'Семпл',
                'verbose_name_plural': 'Семплы',
            },
        ),
    ]
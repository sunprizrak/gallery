# Generated by Django 3.2.3 on 2021-07-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210701_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]

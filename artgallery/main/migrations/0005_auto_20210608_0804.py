# Generated by Django 3.2.3 on 2021-06-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210607_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='virtual',
            options={'ordering': ['title'], 'verbose_name': 'Виртуальная выставка', 'verbose_name_plural': 'Виртуальные выставки'},
        ),
        migrations.AddField(
            model_name='virtual',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='virtual',
            unique_together={('title', 'slug')},
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20210709_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewermodel',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]

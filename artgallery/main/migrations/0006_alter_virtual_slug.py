# Generated by Django 3.2.3 on 2021-06-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210608_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtual',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

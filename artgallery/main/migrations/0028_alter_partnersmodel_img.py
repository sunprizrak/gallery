# Generated by Django 3.2.3 on 2021-06-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_partnersmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnersmodel',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Логотип'),
        ),
    ]

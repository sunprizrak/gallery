# Generated by Django 3.2.3 on 2021-06-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_artistinfo_artistmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Контент для зрителей',
                'verbose_name_plural': 'Контент для зрителей',
            },
        ),
    ]

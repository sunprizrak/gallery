# Generated by Django 3.2.3 on 2021-06-08 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210608_0848'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='virtual',
            unique_together={('title', 'slug')},
        ),
    ]

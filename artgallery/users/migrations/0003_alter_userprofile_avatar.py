# Generated by Django 3.2.3 on 2021-09-17 13:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]

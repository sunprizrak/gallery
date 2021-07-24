from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ArtistModel(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент для художников'
        verbose_name_plural = 'Контент для художников'


class ViewerModel(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст', blank=True)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент для зрителей'
        verbose_name_plural = 'Контент для зрителей'


class AboutModel(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О проекте'
        verbose_name_plural = 'О проекте'


class HistoryModel(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История проекта'
        verbose_name_plural = 'История проекта'


class TogetherModel(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cотрудничество'
        verbose_name_plural = 'Сотрудничество'


class PartnersModel(models.Model):
    title = models.CharField('Название', max_length=50)
    content = RichTextUploadingField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
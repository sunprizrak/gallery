from django.db import models


class Virtual(models.Model):
    title = models.CharField('Название', max_length=50, unique=True)
    field_name_log = models.URLField('URL log', blank=True)
    field_name_nolog = models.URLField('URL nolog', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Виртуальная выставка'
        verbose_name_plural = 'Виртуальные выставки'
        ordering = ['title']

from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import ArtistModel, ViewerModel, AboutModel, HistoryModel, TogetherModel, PartnersModel


class ArtistAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)
    text_en = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = ArtistModel
        fields = '__all__'


class ViewerAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)
    text_en = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = ViewerModel
        fields = '__all__'


class AboutAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)
    text_en = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = AboutModel
        fields = '__all__'


class HistoryAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)
    text_en = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = HistoryModel
        fields = '__all__'


class TogetherAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)
    text_en = forms.CharField(label='текст', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = TogetherModel
        fields = '__all__'


class PartnersAdminForm(forms.ModelForm):
    content = forms.CharField(label='Логотип', widget=CKEditorUploadingWidget(), required=False)

    class Meta:
        model = PartnersModel
        fields = '__all__'


@admin.register(ArtistModel)
class ArtistAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    form = ArtistAdminForm


@admin.register(ViewerModel)
class ViewerAdmin(TranslationAdmin):
    list_display = ('title', 'text', 'lat', 'lon')
    form = ViewerAdminForm


@admin.register(AboutModel)
class AboutAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    form = AboutAdminForm


@admin.register(HistoryModel)
class HistoryAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    form = HistoryAdminForm


@admin.register(TogetherModel)
class TogetherAdmin(TranslationAdmin):
    list_display = ('title', 'text')
    form = TogetherAdminForm


@admin.register(PartnersModel)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    form = PartnersAdminForm
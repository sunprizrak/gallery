from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
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
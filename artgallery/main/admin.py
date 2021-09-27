from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ArtistModel, ViewerModel, AboutModel, HistoryModel, TogetherModel, PartnersModel
from .forms import ArtistAdminForm, ViewerAdminForm, AboutAdminForm, HistoryAdminForm, TogetherAdminForm, \
    PartnersAdminForm


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
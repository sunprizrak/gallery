from modeltranslation.translator import register, TranslationOptions
from .models import HistoryModel, TogetherModel, AboutModel, ArtistModel, ViewerModel


@register(HistoryModel)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(TogetherModel)
class TogetherTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(ArtistModel)
class ArtistTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(ViewerModel)
class ViewerTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
from django.views.generic import ListView, TemplateView
from .models import ArtistModel, ViewerModel, AboutModel, HistoryModel, TogetherModel, PartnersModel


class HomeView(TemplateView,):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Международная выставка искусств | Я Моне Я Шишкин Я Малевич',
    }


class ArtistsView(ListView):
    model = ArtistModel
    template_name = 'main/artists.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Художникам',
    }


class ViewersView(ListView):
    model = ViewerModel
    template_name = 'main/viewers.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Зрителям',
        }


class AboutView(ListView):
    model = AboutModel
    template_name = 'main/about.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'О проекте',
    }


class HistoryView(ListView):
    model = HistoryModel
    template_name = 'main/history.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'История проекта',
    }


class TogetherView(ListView):
    model = TogetherModel
    template_name = 'main/together.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Сотрудничество',
    }


class PartnersView(ListView):
    model = PartnersModel
    template_name = 'main/partners.html'
    context_object_name = 'object'
    extra_context = {
        'title': 'Партнёры',
        }
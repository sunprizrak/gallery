from django.urls import path
from .views import HomeView, AboutView, HistoryView, TogetherView, ViewersView, PartnersView, ArtistsView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('history', HistoryView.as_view(), name='history'),
    path('cooperation', TogetherView.as_view(), name='cooperation'),
    path('viewers', ViewersView.as_view(), name='viewers'),
    path('artists', ArtistsView.as_view(), name='artists'),
    path('partners', PartnersView.as_view(), name='partners'),
]
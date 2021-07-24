from django.urls import path
from .views import VirtualView, VirtualDetailView


urlpatterns = [
    path('', VirtualView.as_view(), name='virtual'),
    path('<slug:slug>', VirtualDetailView.as_view(), name='virtual-detail'),
]
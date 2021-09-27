from django.urls import path

from . import views
from .views import RegisterUserView, LoginUserView, logout_user, PasswordEditView, profile

urlpatterns = [
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('profile', profile, name='profile'),
    path('change-password', PasswordEditView.as_view(), name='change-password'),
]
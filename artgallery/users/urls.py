from django.urls import path
from .views import RegisterUserView, LoginUserView, logout_user


urlpatterns = [
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
]
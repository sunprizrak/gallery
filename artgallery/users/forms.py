from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.forms import TextInput, EmailInput, PasswordInput, CharField, ClearableFileInput
from django.utils.translation import ugettext_lazy as _

from .models import Profile


class RegistrationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Логин'),
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Пароль')})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Повторить пароль')})


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control', 'placeholder': _('Логин')}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Пароль')}))


class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('старый пароль')}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('новый пароль')}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('повторите пароль')}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Имя'),
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Фамилия'),
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

        widgets = {
            'avatar': ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


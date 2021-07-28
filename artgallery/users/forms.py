from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, CharField
from django.utils.translation import ugettext_lazy as _


class RegisterUserForm(UserCreationForm):
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
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Пароль')})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Повторить пароль')})


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control', 'placeholder': _('Логин')}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Пароль')}))

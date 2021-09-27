from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from .forms import RegistrationUserForm, LoginUserForm, UserEditForm, PasswordEditForm, ProfileEditForm
from django.utils.translation import ugettext_lazy as _

from .models import Profile


class RegisterUserView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': _('Регистрация')
    }

    def form_valid(self, form, backend='django.contrib.auth.backends.ModelBackend'):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': _('Авторизация')
    }


def logout_user(request):
    logout(request)
    return redirect('home')


class PasswordEditView(PasswordChangeView):
    form_class = PasswordEditForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserRegisterForm


class UserRegisterView(CreateView):
    """
    Представление для регистрации нового пользователя.
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/register.html'
    extra_context = {'title': 'Регистрация пользователя'}


class UserLoginView(LoginView):
    """
    Представление для входа пользователя в систему.
    """
    template_name = 'user/login.html'
    extra_context = {'title': 'Авторизация'}


class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя из системы.
    """
    pass

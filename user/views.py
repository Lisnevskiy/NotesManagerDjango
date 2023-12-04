from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import UserRegisterForm


class UserRegisterView(CreateView):
    """
    Представление для регистрации нового пользователя.
    Attributes:
        model (Model): Модель пользователя, используемая для регистрации.
        form_class (Form): Форма, используемая для регистрации пользователя.
        success_url (str): URL для перенаправления после успешной регистрации.
        template_name (str): Имя шаблона для отображения формы регистрации.
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/register.html'


class UserLoginView(LoginView):
    """
    Представление для авторизации пользователя.
    Attributes:
        template_name (str): Имя шаблона для отображения формы авторизации.
    """
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя из системы.
    Наследует:
        LogoutView: Встроенное Django представление для выхода пользователя.
    """
    pass

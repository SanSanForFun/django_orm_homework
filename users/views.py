from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail

from users.forms import UserRegisterForm


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('catalog:products_list')

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     self.send_welcome_email(user.email)
    #     return super().form_valid(form)
    #
    # def send_welcome_email(self, email):
    #     subject = 'Добро пожаловать на сайт'
    #     message = 'Спасибо что зарегистрировались на нашем сайте'
    #     from_email = 'user_address@mail.com'
    #     recipient_list = [email]
    #     send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('catalog:products_list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:products_list')

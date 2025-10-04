from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar', 'phone_number', 'country']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        template_name = 'registration/login.html'
        fields = ('email', 'password')
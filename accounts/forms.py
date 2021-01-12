from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.urls import reverse_lazy


class SignUpForm(UserCreationForm):

    class Meta:
        form_class = UserCreationForm
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'class_name',)

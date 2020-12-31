from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class SignUpForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2', 'class_name',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'Nazwa użytkownika'
    #     self.fields['username'].help_text = None
    #     self.fields['password1'].label = 'Hasło'
    #     self.fields['password1'].help_text = None
    #     self.fields['password2'].label = 'Powtórz hasło'
    #     self.fields['password2'].help_text = None
    #     self.fields['class_name'].label = 'Klasa'
    #     self.fields['class_name'].help_text = None

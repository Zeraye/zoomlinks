from django import forms
from accounts.models import UserProfile

class SettingsForm(forms.Form):

    class Meta:
        model = UserProfile

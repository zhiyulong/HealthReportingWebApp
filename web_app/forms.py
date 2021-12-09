from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.EmailField(max_length=120, help_text='Enter student email address.')
    name = forms.CharField(max_length=50, required=False)
    nuid = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'nuid', 'password1', 'password2')
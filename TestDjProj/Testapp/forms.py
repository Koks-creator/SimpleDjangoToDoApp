from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewList(forms.Form):#"form-control
    name = forms.CharField(label="Name of the list", max_length=200, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'})
                           )


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
# accounts/forms.py
from django import forms
from .models import UserRegistration


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'image', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Логин или Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomModel
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomModel
        fields = UserChangeForm.Meta.fields

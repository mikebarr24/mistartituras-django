from django import forms
from django.forms import ModelForm

from .models import Part


class NewUserForm(forms.Form):
    username = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': "Username"}))
    name = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': "Nombre"}))
    email = forms.EmailField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Password"}), label="")
    password_verify = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Re-Enter Password"}), label="")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': "Password"}), label="")


class PartForm(ModelForm):

    class Meta:
        model = Part
        fields = ["part_title", "composer_name", "instrument",
                  "level", "style", "curso", "pdf", "audio"]

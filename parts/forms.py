from django import forms
from django.forms import ModelForm

from .models import Part, Level


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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': "Name"}))
    email = forms.CharField(max_length=30, label="", widget=forms.TextInput(
        attrs={'placeholder': "Email"}))
    message = forms.CharField(max_length=30, label="", widget=forms.Textarea(
        attrs={'placeholder': "Message"}))


class PartForm(ModelForm):

    class Meta:
        model = Part
        fields = ["part_title", "composer_name", "instrument",
                  "level", "style", "curso", "pdf", "audio"]

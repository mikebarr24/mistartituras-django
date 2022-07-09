from django import forms


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

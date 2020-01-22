from django import forms

# --------------------------------------------------------- User Login Form
class LoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# --------------------------------------------------------- Member Join in Form


class JoinForm(UserCreationForm):

    password1 = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = ['email', 'username', 'password1', 'password2']
        fields = ['firstName', 'lastName', 'username', 'dob',
                  'email', 'password1', 'password2',
                  'address1', 'address2', 'town', 'postcode',
                  'landline', 'mobile']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(
                'This email address is already registered. Please use a different one.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password.")

        if password1 != password2:
            raise ValidationError("Both passwords must match.")

        return password2

# --------------------------------------------------------- User Login Form


class LoginForm(forms.Form):

    username = forms.CharField(max_length=50, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus import DatePickerInput

# --------------------------------------------------------- Member Join in Form


class JoinForm(UserCreationForm):

    first_name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    dob = forms.DateField(widget=DatePickerInput(format='%d/%m/%Y',
                                                 options={
                                                     'showTodayButton': False,
                                                     'showClear': False,
                                                 }))
    # email = forms.EmailField(max_length=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    address1 = forms.CharField(max_length=100, label='Home address')
    address2 = forms.CharField(max_length=100, label='Home address (Optional)',
                               required=False)
    postcode = forms.CharField(max_length=20)
    town = forms.CharField(max_length=50)
    landline = forms.CharField(label='Home phone number (Optional)',
                               required=False)
    mobile = forms.CharField(label='Mobile number')
    date = forms.DateInput()

    class Meta:
        model = User
        fields = ['first_name', 'surname', 'dob', 'email',
                  'username', 'password1', 'password2',
                  'address1', 'address2', 'postcode', 'town',
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

    username_or_email = forms.CharField(max_length=50, label="Email address")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")

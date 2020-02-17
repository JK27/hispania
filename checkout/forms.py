from django import forms
from django.utils import timezone
from .models import Order
from bootstrap_datepicker_plus import MonthPickerInput, YearPickerInput

# --------------------------------------------------------- Payment form


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2050)]
    today = timezone.now

    credit_card_number = forms.CharField(label="Credit card number",
                                         required=False)
    cvv = forms.CharField(label="Security code", required=False)
    expiry_month = forms.DateField(widget=MonthPickerInput(format='%m',
                                   options={
                                       'showTodayButton': False,
                                       'showClear': False,
                                   }))
    expiry_year = forms.DateField(widget=YearPickerInput(format='%Y'))
    # expiry_month = forms.ChoiceField(label="Expiry month", choices=MONTH_CHOICES,
    #                                  required=False)
    # expiry_year = forms.ChoiceField(label="Expiry year", choices=YEAR_CHOICES,
    #                                 required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# --------------------------------------------------------- Order form


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'surname', 'email_address',
                  'address1', 'address2', 'postcode',
                  'town', 'landline', 'mobile')

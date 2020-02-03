from django import forms
from .models import Order

# --------------------------------------------------------- Payment form


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2050)]

    credit_card_number = forms.CharField(label="Credit card number",
                                         required=False)
    cvv = forms.CharField(label="Security code", required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# --------------------------------------------------------- Order form


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'surname', 'address1', 'address2',
                  'postcode', 'town', 'county', 'phone_number',
                  'email_address')

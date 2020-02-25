from django.db import models
from memberships.models import Membership


class Order(models.Model):
    first_name = models.CharField(max_length=100, blank=False, default='')
    surname = models.CharField(max_length=100, blank=False, default='')
    email_address = models.EmailField(max_length=100, blank=False, default='')
    address1 = models.CharField(max_length=100, blank=False, default='',
                                verbose_name='Home address')
    address2 = models.CharField(max_length=100, blank=True, default='',
                                verbose_name='Home address (Optional)')
    postcode = models.CharField(max_length=20, blank=True, default='')
    town = models.CharField(max_length=50, blank=False, default='')
    landline = models.IntegerField(blank=True, default='',
                                   verbose_name='Home phone number (Optional)')
    mobile = models.IntegerField(blank=False, default='',
                                 verbose_name='Mobile number', )
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date,
                                    self.first_name, self.surname)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, null=False,
                                   on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity,
                                      self.membership.membership_type,
                                      self.membership.price)

from django.db import models
from memberships.models import Membership


class Order(models.Model):
    first_name = models.CharField(max_length=100, blank=False, default='')
    surname = models.CharField(max_length=100, blank=False, default='')
    email_address = models.CharField(max_length=100, blank=False, default='')
    address1 = models.CharField(max_length=100, blank=False, default='')
    address2 = models.CharField(max_length=100, blank=True, default='')
    postcode = models.CharField(max_length=20, blank=True, default='')
    town = models.CharField(max_length=50, blank=False, default='')
    landline = models.CharField(max_length=20, blank=False, default='')
    mobile = models.CharField(max_length=20, blank=False, default='')
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, null=False,
                                   on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity,
                                      self.membership.membership_type,
                                      self.membership.price)

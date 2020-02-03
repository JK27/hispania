from django.db import models
from memberships.models import Membership


class Order(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email_address = models.CharField(max_length=100, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=50, blank=False)
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

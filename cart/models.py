from django.db import models


class Cart(models.Model):

    def __str__(self):
        return self.cart

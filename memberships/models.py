from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# --------------------------------------------------------- Show memberships


class Membership(models.Model):
    category = models.ManyToManyField(Category)
    membership_type = models.CharField(max_length=50, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(default=membership_type)

    def __str__(self):
        return self.membership_type

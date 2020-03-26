from django.db import models

# --------------------------------------------------------- Show memberships


class Membership(models.Model):
    membership_type = models.CharField(max_length=50, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(default=membership_type)

    def __str__(self):
        return self.membership_type

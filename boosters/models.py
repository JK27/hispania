from django.db import models

# --------------------------------------------------------- Show all boosters


class Booster(models.Model):
    booster = models.CharField(max_length=50, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.booster

from django.db import models


# --------------------------------------------------------- Categories
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# --------------------------------------------------------- Memberships
class Membership(models.Model):
    membership_type = models.CharField(max_length=50, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.membership_type

from django.contrib import admin
from .models import Booster

# --------------------------------------------------------- Boosters Admin
class BoosterAdmin(admin.ModelAdmin):
    list_display = ('booster', 'description', 'price', 'id')


admin.site.register(Booster, BoosterAdmin)

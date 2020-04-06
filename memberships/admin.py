from django.contrib import admin
from .models import Membership, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')


admin.site.register(Category, CategoryAdmin)


# --------------------------------------------------------- Memberships Admin
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_type', 'description',
                    'price', 'id')


admin.site.register(Membership, MembershipAdmin)

from django.contrib import admin
from .models import Membership, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


# --------------------------------------------------------- Memberships Admin
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_type', 'category', 'description',
                    'price', 'id')
    prepopulated_fields = {'slug': ('membership_type',)}


admin.site.register(Membership, MembershipAdmin)

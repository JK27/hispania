from django.contrib import admin
from .models import Membership


# --------------------------------------------------------- Memberships Admin
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_type', 'description', 'price', 'id')


admin.site.register(Membership, MembershipAdmin)

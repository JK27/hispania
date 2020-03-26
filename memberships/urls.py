from django.urls import path
from .views import list_memberships, detail_membership

urlpatterns = [
    path('', list_memberships, name="memberships"),
    path('<slug>', detail_membership, name="detail_membership")
]

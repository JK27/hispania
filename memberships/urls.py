from django.urls import path
from .views import list_memberships, detail_membership, list_categories

urlpatterns = [
    path('', list_memberships, name="list_memberships"),
    path('<slug>', detail_membership, name="detail_membership")
]

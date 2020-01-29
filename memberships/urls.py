from django.urls import path
from .views import all_memberships

urlpatterns = [
    path('', all_memberships, name="memberships"),
]

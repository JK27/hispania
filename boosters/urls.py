from django.urls import path
from .views import all_boosters

urlpatterns = [
    path('', all_boosters, name="boosters"),
]

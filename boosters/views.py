from django.shortcuts import render
from .models import Booster


def all_boosters(request):
    boosters = Booster.objects.all()
    return render(request, "boosters.html", {"boosters": boosters})

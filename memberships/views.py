from django.shortcuts import render, get_object_or_404
from .models import Membership


def list_memberships(request):
    all_memberships = Membership.objects.all()
    context = {"all_memberships": all_memberships}
    return render(request, "memberships.html", context)


def detail_membership(request, slug):
    membership = get_object_or_404(Membership, slug=slug)
    context = {'membership': membership}

    return render(request, "membership_detail.html", context)

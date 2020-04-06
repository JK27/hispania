from django.shortcuts import render, get_object_or_404
from .models import Membership, Category


# --------------------------------------------------------- Categories list
def list_categories(request, slug):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, "categories.html", context)


# --------------------------------------------------------- Memberships list
def list_memberships(request, category_slug=None):
    categories = Category.objects.all()
    memberships = Membership.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        memberships = memberships.filter(category=category)
    context = {'categories': categories, "memberships": memberships}
    return render(request, "memberships.html", context)


# --------------------------------------------------------- Memberships detail
def detail_membership(request, slug):
    membership = get_object_or_404(Membership, slug=slug)
    context = {'membership': membership}

    return render(request, "membership_detail.html", context)

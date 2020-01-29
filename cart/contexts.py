from django.shortcuts import get_object_or_404
from memberships.models import Membership


def cart_contents(request):
    """
    Allows cart contents to display when rendering any page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    items_count = 0
    for id, quantity in cart.items():
        membership = get_object_or_404(Membership, pk=id)
        total += quantity * membership.price
        items_count += quantity
        cart_items.append({'id': id,
                           'quantity': quantity,
                           'membership': membership})

    return {'cart_items': cart_items,
            'total': total,
            'items_count': items_count}

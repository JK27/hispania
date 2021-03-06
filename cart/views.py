from django.shortcuts import render, redirect, reverse


# --------------------------------------------------------- View Cart
def view_cart(request):
    # Renders cart contents page
    return render(request, "cart.html")


# --------------------------------------------------------- Add to Cart
def add_to_cart(request, id):
    # Adds quantity of specified item to cart
    quantity = int(request.POST.get('quantity'))
    cart = {id: quantity}

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# --------------------------------------------------------- Remove from Cart
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] -= 1
        if cart[id] == 0:
            del cart[id]
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

from django.shortcuts import render, redirect, reverse


# --------------------------------------------------------- View Cart
def view_cart(request):
    # Renders cart contents page
    return render(request, "cart.html")


# --------------------------------------------------------- Add to Cart
def add_to_cart(request, id):
    # Adds quantity of specified item to cart
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = 1
        # cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# --------------------------------------------------------- Remove from Cart
def remove_from_cart(request, id):
    # Adjusts quantity of specified item to specified amount
    # quantity = int(request.POST.get('quantity'))
    # cart = request.session.get('cart', {})

    # if quantity > 0:
    #     cart[id] = quantity
    # else:
    #     cart.pop(id)

    # request.session['cart'] = cart
    # return redirect(reverse('view_cart'))
    ########################################################################
    # Removes quantity of specified item to cart
    # quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] -= 1
        if cart[id] == 0:
            del cart[id]
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

from django.shortcuts import render
from django.contrib.auth import login as auth_login
from cart.cart import Cart
from .models import OrderItem, Order
from .forms import OrderCreateForm
from users.models import User

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():

            #creating a new user alongside the order
            user = User.objects.create_user(
                email = form.cleaned_data.get('email'),
                name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                password = form.cleaned_data.get('password')
            )
            user.save()
            #update user fields to be used for the next order
            user.address = form.cleaned_data.get('address')
            user.postal_code = form.cleaned_data.get('postal_code')
            user.city = form.cleaned_data.get('city')
            auth_login(request, user)
            order = form.save()
            
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})

def make_order(request):
    #used to create orders for when a user is logged in
    cart = Cart(request)
    owner = request.user
    order = Order.objects.create(
            user = owner,
            first_name = owner.first_name,
            last_name = owner.last_name,
            email = owner.email,
            address = owner.address,
            postal_code = owner.postal_code,
            city = owner.city
    )
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'],
                                    price=item['price'], quantity=item['quantity'])
    # clear the cart
    cart.clear()
    return render(request, 'order/created.html', {'order': order})

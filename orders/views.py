from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Order, OrderItem
from .tasks import order_created
from django.urls import reverse


def orders_add(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                              product=item['product'],
                                              price=item['price'],
                                              quantity=item['quantity'])
                cart.clear()
                order_created.delay(order.id)
                request.session['order_id'] = order.id
                return redirect(reverse('payment:process'))
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
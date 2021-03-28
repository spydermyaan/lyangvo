from .models import Product, Cart
from django.shortcuts import redirect, render


def store(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'store/store.html', context)


def cart(req):
    cart = Cart.objects.all()
    items = []
    products = []
    for c in cart:
        items.append({
            "items": c.product
        })
    for i in items:
        products = Product.objects.filter(product_title=i)
    # context = {"items": items}
    return render(req, 'store/cart.html', {'items': products})


def checkout(req):
    context = {}
    return render(req, 'store/checkout.html', context)


def add_to_cart(req, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart()
    cart.save()
    cart.product.add(product)
    return redirect('store')

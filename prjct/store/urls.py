from django.urls import path
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('add/<str:product_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout")
]

"""
URL configuration for arrayshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import urls as shop_urls
from cart import urls as cart_urls
from orders import urls as orders_urls
from payment import urls as payment_urls
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('shop/', include(shop_urls, namespace='shop')),
#     path('cart/', include(cart_urls, namespace='cart')),
#     path('orders/', include(orders_urls, namespace='orders')),
#     path('payment/', include(payment_urls, namespace='payment'))
# ] + debug_toolbar_urls()

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                             document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include(shop_urls, namespace='shop')),
    path('cart/', include(cart_urls, namespace='cart')),
    path('orders/', include(orders_urls, namespace='orders')),
    path('payment/', include(payment_urls, namespace='payment')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

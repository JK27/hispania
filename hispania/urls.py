from django.contrib import admin
from django.urls import path, include
from home import views
from accounts import urls as urls_accounts
from memberships import urls as urls_memberships
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.index, name="index"),
    path('accounts/', include(urls_accounts)),
    path('memberships/', include(urls_memberships)),
    path('cart/', include(urls_cart)),
    path('checkout/', include(urls_checkout)),
    path('media/(?<path>.*)', static.serve, {'document_root': MEDIA_ROOT}),
]

"""config URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include,re_path

urlpatterns = [
    path('', include('shop.urls', namespace='shop')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('users/',include('users.urls', namespace='users'))
]
urlpatterns += [ re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]

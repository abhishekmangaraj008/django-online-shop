from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import register

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cart/', include('cart.urls')),

    path('orders/', include('orders.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('register/', register, name='register'),

    path('', include('shop.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from config.settings import IS_DEVELOPMENT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('users.urls')),
    path('subs/', include('subscriptions.urls')),
    path('payments/', include('payments.urls')),
]

if IS_DEVELOPMENT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Store app URLs
    path('', include('store.urls')),

    # Cart app URLs
    path('cart/', include('cart.urls')),

    # Account app
    path('account/', include('account.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('keyval/', include('key_val_api.urls')),
    path('dogs/', include('dogs_api.urls')),
]

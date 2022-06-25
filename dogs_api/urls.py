from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.DogInfoList.as_view(), name='list'),
    path('<int:pk>/', views.DogImagesMod.as_view(), name='dog-info'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
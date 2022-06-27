from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('howto/keyval', views.howto_keyval, name='howto-keyval'),
]

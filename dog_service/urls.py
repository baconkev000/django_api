from django.urls import path
from . import views

urlpatterns = [
    path('', views.DogsAPIInfo.as_view(), name="dogs"),
]

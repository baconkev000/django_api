from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.KeyValueList.as_view(), name="list"),
    path('<int:pk>', views.KeyValueDetail.as_view(), name="kv-detail"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.DogInfoList.as_view(), name="list"),
    path('<int:pk>/', views.DogImagesMod.as_view(), name="detail")
]   

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.KeyValueList.as_view(), name="list"),
    path('<keyParam>', views.KeyValueDetail.as_view(), name="kv-detail"),
    path('delete/<keyParam>', views.KeyValueDelete.as_view(), name="delete"),
    path('delete/id/<int:pk>', views.KeyValueDeletePK.as_view(), name="deletepk"),
]

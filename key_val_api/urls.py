from django.urls import path
from . import views

urlpatterns = [
    path('list', views.KeyValueList.as_view(), name="list"),
    path('create', views.CreateKeyVal.as_view(), name="create-keyval"),
    path('<keyParam>', views.GetKeyVal.as_view(), name="kv-detail"),
    path('<keyParam>', views.IncrementKeyVal.as_view(), name="kv-detail"),
    path('delete/<keyParam>', views.KeyValDeleteByKeyName.as_view(), name="deletekey"),
    path('delete/id/<int:pk>', views.KeyValueDeleteByID.as_view(), name="deletepk"),
]

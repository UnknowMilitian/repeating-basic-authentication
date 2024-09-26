from django.urls import path
from .views import ItemListAPIView, RegisterView

urlpatterns = [
    path("item-list", ItemListAPIView.as_view(), name="item-list"),
    path("register/", RegisterView.as_view(), name="register"),
]

# item/urls.py
from django.urls import path 
from .views import ItemListView, ItemDetailView, ItemUpdateView, ItemCreateView, ItemDeleteView

urlpatterns = [
    path("items/", ItemListView.as_view(), name="list_item"),
    path("items/<int:pk>/detail/", ItemDetailView.as_view(), name="detail_item"), 
    path("items/<int:pk>/edit/", ItemUpdateView.as_view(), name= "update_item"), 
    path("items/new/", ItemCreateView.as_view(), name= "new_item"), 
    path("items/<int:pk>/delete/", ItemDeleteView.as_view(), name= "new_item"),
]
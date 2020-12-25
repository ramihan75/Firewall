#posts/urls.py
from django.urls import path 
from .views import BookListView, BookDetailView

urlpatterns = [
    path("book/<int:pk>/", BookDetailView.as_view(), name="detail_book"),
    path("", BookListView.as_view(), name="home"),
]
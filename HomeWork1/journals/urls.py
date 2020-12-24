#posts/urls.py
from django.urls import path 
from .views import JournalListView, JournalDetailView

urlpatterns = [
    path("journal/<int:pk>/", JournalDetailView.as_view(), name="detail_journal"),
    path("", JournalListView.as_view(), name="home"),
]
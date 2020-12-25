from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView, DetailView 

# Create your views here.

class JournalListView(ListView):
    model = Journal
    template_name = "home.html"
    context_object_name = "journals"

class JournalDetailView(DetailView):
    model = Journal 
    template_name = "detail_journal.html"
    context_object_name = "journal"

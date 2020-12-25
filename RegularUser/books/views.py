from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView 

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book 
    template_name = "detail_book.html"
    context_object_name = "book"

       

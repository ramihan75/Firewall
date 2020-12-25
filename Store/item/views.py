from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView 
from .models import Item
from django.urls import reverse_lazy 

class ItemListView(ListView):
    model = Item
    template_name = "list_item.html"
    context_object_name = "list_item"

class ItemDetailView(DetailView):
    model = Item 
    template_name = "detail_item.html"
    context_object_name = "item"

class ItemUpdateView(UpdateView):
    model = Item 
    fields = ("title", "amount", "price")
    template_name = "update_item.html"

class ItemCreateView(CreateView):
    model = Item
    template_name = "new_item.html"
    fields = ('title', 'price', 'owner') 

class ItemDeleteView(DeleteView):
    model = Item
    template_name = "delete_item.html"
    success_url = reverse_lazy("list_item")   

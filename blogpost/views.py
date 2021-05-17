from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogModel

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')

from django.views import generic

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# class BlogList(generic.TemplateView):
#     template_name = 'list.html'
#     model = BlogModel

# Create your views here.

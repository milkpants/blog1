from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogModel

from django.views import generic


class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

# class BlogList(generic.TemplateView):
#     template_name = 'list.html'
#     model = BlogModel

# Create your views here.

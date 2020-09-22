from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView



class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

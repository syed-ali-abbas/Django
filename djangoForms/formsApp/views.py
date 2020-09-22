from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy



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


class BlogUpdate(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']


class BlogDeletion(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class HomepageView(ListView):
    model = Post
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'post.html'
    success_url = reverse_lazy('home')
    fields = '__all__'



class UpdateHomepage(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post_delete.html'
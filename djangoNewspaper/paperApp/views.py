from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import CustomModel
from django.urls import reverse_lazy



class signupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class HomePageView(TemplateView):
    template_name = 'home.html'

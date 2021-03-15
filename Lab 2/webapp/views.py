from django.shortcuts import render
from django.views.generic import ListView
from .models import Hacker


class BasePageView(ListView):
    model = Hacker
    template_name='base.html'

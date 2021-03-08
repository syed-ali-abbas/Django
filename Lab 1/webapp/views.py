from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogPageView(ListView):
    model = Post
    template_name = 'blogs.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detailed_posts.html'





# def get(self, request):
#     if not cart:
#         products = None
        
#         categoryid = request.GET.get('Post')
#     if categoryid:
#         products = Product.get_all_ProductsByCategory(categoryid)
#     else:
#         products = Product.get_all_products()

#     data_dictionary = {
#         'products': products,
#         'category': categories
#     }
#     return render(request, 'blogs.html', data_dictionary)



    
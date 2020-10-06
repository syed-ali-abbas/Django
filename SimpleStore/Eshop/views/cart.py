from django.views import View
from django.shortcuts import render
from Eshop.models.Product import Product
# from Eshop.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator


class cart(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request,'cart.html', {'products':products})

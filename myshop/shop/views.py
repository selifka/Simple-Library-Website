"""
This is the cart view functions
File: views.py
Author: Bonnie
Date: 11/11/2016
"""

from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    """
    This creates categoy of products and it filter by category.  
    """
    category = None
    query_text = request.GET.get('search_term')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if query_text:
        products = products.filter(name__icontains=query_text)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def home(request):
    """
    It shows home screen. 
    """
    if 'search_term' in request.GET:
        return redirect('/?search_term={}'.format(request.GET['search_term']))
    return render(request, 'shop/home.html', {})


def product_detail(request, id, slug):
    """
    It shows product detail page.
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})

from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


# Create your views here.
class HomePageView(ListView):
    model = Product
    template_name = 'main__index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')


class IndexPageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')

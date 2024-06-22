from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.cache import cache

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
    template_name = 'catalog.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-id')


# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     return render(request, 'type_of_furniture.html', {'product': product})
#

class ProductDetail(DetailView):
    model = Product
    template_name = 'type_of_furniture.html'
    context_object_name = 'product'

    # def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта
    #     obj = cache.get(f'product-{self.kwargs["pk"]}', None)
    #
    #     # если объекта нет в кэше, то получаем его и записываем в кэш
    #     if not obj:
    #         obj = super().get_object(queryset=self.queryset)
    #         cache.set(f'product-{self.kwargs["pk"]}', obj)
    #
    #     return obj

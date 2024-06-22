from django.urls import path
from .views import HomePageView, IndexPageView, ProductDetail
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('catalog/', IndexPageView.as_view(), name='index'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    # path('<int:pk>', cache_page(60*10)(ProductDetail.as_view()), name='product_detail'),
]
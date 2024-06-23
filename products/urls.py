from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, IndexPageView, ProductDetail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('catalog/', IndexPageView.as_view(), name='index'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    # path('<int:pk>', cache_page(60*10)(ProductDetail.as_view()), name='product_detail'),  # use cache
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
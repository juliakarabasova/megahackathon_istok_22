from django.urls import path
from .views import HomePageView, IndexPageView

urlpatterns = [
   path('', HomePageView.as_view(), name='home'),
   path('index/', IndexPageView.as_view(), name='index'),
]
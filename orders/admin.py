from django.contrib import admin
from .models import Order, OrderTimeline

admin.site.register(Order)
admin.site.register(OrderTimeline)

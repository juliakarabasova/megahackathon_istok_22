from django.contrib import admin
from .models import CustomUser, LoyaltyTransaction, Referal, Promotion, News

admin.site.register(CustomUser)
admin.site.register(LoyaltyTransaction)
admin.site.register(Referal)
admin.site.register(Promotion)
admin.site.register(News)

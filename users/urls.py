from django.urls import path
from .views import SignUp, personal_account_profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('personal-account-profile/', personal_account_profile, name='profile'),
]
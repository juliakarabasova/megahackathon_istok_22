from django.urls import path
from .views import SignUp, personal_account_profile, create_or_login_user

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('personal-account-profile/', personal_account_profile, name='profile'),
    path('api/create-or-login-user/', create_or_login_user, name='create_or_login_user'),
]
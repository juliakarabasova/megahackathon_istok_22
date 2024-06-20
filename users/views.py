from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


def personal_account_profile(request):
    return render(request, 'personalAccountProfile.html')

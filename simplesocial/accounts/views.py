from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import (CreateView)
# from accounts.models import User


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    #reverse lazy cause it waits for user to hit sign up, reverse will directly take
    template_name = 'accounts/signup.html'

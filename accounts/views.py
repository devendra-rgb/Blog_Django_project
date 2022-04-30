from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name='signup.html'
    success_url=reverse_lazy('login')

# Create your views here.

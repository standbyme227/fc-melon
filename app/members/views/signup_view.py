from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from datetime import datetime

from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests

from members.forms import SignupForm

User = get_user_model()

__all__ = (
    'signup_view',
)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    context = {
        'signup_form': form,
    }
    return render(request, 'members/signup.html', context)

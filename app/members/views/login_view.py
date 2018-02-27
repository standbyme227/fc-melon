from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from datetime import datetime

from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests

from members.forms import SignupForm

User = get_user_model()

__all__ = (
    'login_view',
)


# 장고가 쓰고있는 user_model을 가져온다.

def login_view(request):
    # login 뷰를 작성하는 거다. 이제서야 의문인게 request는 받는다 라는 건가????
    if request.method == 'POST':
        username = request.POST['username']
        # POST는 queryset이다. 근데 queryset이 정확히 뭔가?/?
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'members/login.html')

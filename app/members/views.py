from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from datetime import datetime

from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests

from members.forms import SignupForm

User = get_user_model()


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



def logout_view(request):
    logout(request)
    return redirect('index')


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

    #     username = request.POST['username']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']
    #
    #     is_valid = True
    #     if User.objects.filter(username=username).exists():
    #         context['errors'].append('Username already exists')
    #         is_valid = False
    #     if password != password2:
    #         context['errors'].append('Password and Password2 is not equal')
    #         is_valid = False
    #     if is_valid:
    #         User.objects.create_user(username=username, password=password)
    #         return redirect('index')
    # return render(request, 'members/signup.html', context)



    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['user-email']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']
    #
    #
    #
    #     is_valid = True
    #     if User.objects.filter(username=username).exist():
    #         context['errors'].append('Username already exist')
    #         is_valid = False
    #     if password != password2:
    #         context['errors'].append('Password adn PassWord2 is not equal')
    #         is_valid = False
    #     else:
    #         User.objects.create_user(username, email, password)
    #         return redirect('index')
    #
    #     # elif password == password2:
    #     #     User.objects.create_user(username, email, password,)
    #     #     user = authenticate(request, username=username, password=password)
    #     #     login(request, user)
    #     #     return redirect('index')
    # return render(request, 'members/signup.html', context)

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from datetime import datetime

from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests


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

    # def artist_add(request):
    #     if request.method == 'POST':
    #         name = request.POST['name']
    #         real_name = request.POST['real-name']
    #         nationality = request.POST['nationality']
    #         birth_date = request.POST['birth-date']
    #         constellation = request.POST['constellation']
    #         blood_type = request.POST['blood-type']
    #         intro = request.POST['intro']
    #
    #         Artist.objects.create(
    #             name=name,
    #             real_name=real_name,
    #             nationality=nationality,
    #             birth_date=datetime.datetime.strptime(birth_date, '%Y-%m-%d'),
    #             constellation=constellation,
    #             blood_type=blood_type,
    #             intro=intro
    #         )
    #         return redirect('artist:artist-list')
    #     elif request.method == 'GET':
    #         # elif request.method == 'GET':
    #         #     pass
    #         return render(request, 'artist/artist_add.html')

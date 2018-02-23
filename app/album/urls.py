from django.urls import path, re_path
from . import views

app_name='album'
urlpatterns = [
    path('', views.album_list, name='album-list'), #명시적인 거임?????
]
from django.urls import path, re_path
from . import views

app_name='song'
urlpatterns = [
    path('', views.album_list, name='album-list'), #명시적인 거임?????
]
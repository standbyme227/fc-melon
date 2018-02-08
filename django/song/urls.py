from django.urls import path, re_path
from . import views

app_name='song'
urlpatterns = [
    path('', views.song_list, name='song-list'),
]



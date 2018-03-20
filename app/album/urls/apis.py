from django.urls import path, re_path
from .. import apis

# app_name = 'album'
urlpatterns = [
    path('', apis.album.album_list, name='album-list')
]


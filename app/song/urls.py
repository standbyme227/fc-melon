from django.urls import path, re_path
from . import views

app_name='song'
urlpatterns = [
    path('', views.song_list, name='song-list'),
    path('search/', views.song_search, name='song-search'),
    path('add/melon', views.song_add_from_melon, name='song-add-from-melon'),
    path('search/melon', views.song_search_from_melon, name='song-search-from-melon'),
]



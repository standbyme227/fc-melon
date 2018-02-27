from django.urls import path, re_path
from . import views

app_name='song'
urlpatterns = [
    path('', views.song_list, name='song-list'),
    path('add/', views.song_add, name='song-add'),
    path('edit/<int:song_pk>', views.song_edit, name='song-edit'),
    path('<int:song_pk>', views.song_detail, name='song-detail'),
    path('search/', views.song_search, name='song-search'),
    path('like_toggle/<int:song_pk>', views.song_like_toggle, name='song-like-toggle'),
    path('add/melon', views.song_add_from_melon, name='song-add-from-melon'),
    path('search/melon', views.song_search_from_melon, name='song-search-from-melon'),
]



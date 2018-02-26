from django.urls import path, re_path
from . import views

app_name='artist'
urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('add/', views.artist_add, name='artist-add'),
    path('edit/<int:artist_pk>', views.artist_edit, name='artist-edit'),
    path('like_toggle/<int:artist_pk>', views.artist_like_toggle, name='artist-like-toggle'),
    path('search/melon/', views.artist_search_from_melon, name='artist-search-from-melon'),
    path('add/melon', views.artist_add_from_melon, name='artist-add-from-melon'),
]
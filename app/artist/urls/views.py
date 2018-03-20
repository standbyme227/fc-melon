from django.urls import path, re_path
from .. import views

app_name='artist'
urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('add/', views.artist_add, name='artist-add'),
    path('<int:artist_pk>', views.artist_detail, name='artist-detail'),
    path('edit/<int:artist_pk>', views.artist_edit, name='artist-edit'),
    path('delete/<int:artist_pk>', views.artist_delete, name='artist-delete'),
    path('like_toggle/<int:artist_pk>', views.artist_like_toggle, name='artist-like-toggle'),
    path('add_youtube/<int:artist_pk>', views.artist_add_youtube, name='artist-add-youtube'),
    path('search/melon/', views.artist_search_from_melon, name='artist-search-from-melon'),
    path('add/melon', views.artist_add_from_melon, name='artist-add-from-melon'),
    # path('test/<str:artist_name>', views.get_search_list, name='get-search-list'),
]
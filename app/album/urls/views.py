from django.urls import path, re_path
from .. import views

app_name='album'
urlpatterns = [
    path('', views.album_list, name='album-list'), #명시적인 거임?????
    path('add/', views.album_add, name='album-add'),
    path('edit/<int:album_pk>', views.album_edit, name='album-edit'),
    path('delete/<int:album_pk>', views.album_delete, name='album-delete'),
    path('<int:album_pk>', views.album_detail, name='album-detail'),
    # path('search/', views.album_search, name='album-search'),
    path('like_toggle/<int:album_pk>', views.album_like_toggle, name='album-like-toggle'),
    path('add/melon', views.album_add_from_melon, name='album-add-from-melon'),
    path('search/melon', views.album_search_from_melon, name='album-search-from-melon'),
]

from django.urls import path, re_path
from . import views

app_name='artist'
urlpatterns = [
    path('', views.artist_list, name='artist-list'),
]
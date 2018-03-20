from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from ..apis.artist.list import ArtistList, ArtistDetail

# app_name = 'artist'

urlpatterns = [
    path('', ArtistList.as_view(), name='artist-list'),
    path('<int:pk>/', ArtistDetail.as_view(), name='artist-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from datetime import datetime
import re

from bs4 import BeautifulSoup, NavigableString
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests
from io import BytesIO

from ...models import Song
from ...models import Album
from ...models import Artist

__all__ = (
    'song_add_from_melon',
)


def song_add_from_melon(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        Song.objects.update_or_create_from_melon(song_id)

        return redirect('song:song-list')


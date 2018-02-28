from django.conf import settings
from django.shortcuts import render, redirect
from pip._vendor import requests

from ...models import Artist

__all__ = (
    'artist_detail',
)


def artist_detail(request, artist_pk):
    # artist = get_object_or_404

    artist = Artist.objects.get(pk=artist_pk)

    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': settings.YOUTUBE_API_KEY,
        'part': 'snippet',
        'maxResults': '10',
        'type': 'video',
        'q': artist.name,
    }
    response = requests.get(url, params)
    response_dict = response.json()


    if request.method == 'POST':

        next_path = request.POST.get('next-path', 'artist:artist-detail')
        return redirect(next_path)


    context = {
        'artist': artist,
        'youtube_items': response_dict['items']
    }
    return render(request, 'artist/artist_detail.html', context, )

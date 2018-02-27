import datetime
from django.shortcuts import render, redirect, get_object_or_404
from ...models import Artist


def artist_like_toggle(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    if request.method == 'POST':
        artist.toggle_like_user(user=request.user)
        next_path = request.POST.get('next-path', 'artist:artist-list')
        return redirect(next_path)

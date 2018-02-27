import datetime
from django.shortcuts import render, redirect, get_object_or_404
from ...models import Album


def album_like_toggle(request, album_pk):
    album = Album.objects.get(pk=album_pk)
    if request.method == 'POST':
        album.toggle_like_user(user=request.user)
        next_path = request.POST.get('next-path', 'album:album-list')
        return redirect(next_path)

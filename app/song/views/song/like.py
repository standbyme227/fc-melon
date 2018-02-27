import datetime
from django.shortcuts import render, redirect, get_object_or_404
from ...models import Song


def song_like_toggle(request, song_pk):
    song = Song.objects.get(pk=song_pk)
    if request.method == 'POST':
        song.toggle_like_user(user=request.user)
        next_path = request.POST.get('next-path', 'song:song-list')
        return redirect(next_path)
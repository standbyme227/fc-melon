from django.shortcuts import render, redirect, get_object_or_404
from ...models import Song

__all__ = (
    'song_delete',
)


def song_delete(request, song_pk):
    song = Song.objects.get(pk=song_pk)
    song.delete()
    return redirect('song:song-list')

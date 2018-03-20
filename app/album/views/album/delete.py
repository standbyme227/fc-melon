from django.shortcuts import render, redirect, get_object_or_404
from ...models import Album

__all__ = (
    'album_delete',
)


def album_delete(request, album_pk):
    album = Album.objects.get(pk=album_pk)
    album.delete()
    return redirect('album:album-list')

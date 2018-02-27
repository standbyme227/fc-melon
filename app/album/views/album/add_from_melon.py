from django.shortcuts import render, redirect

from ...models import Album

__all__ = (
    'album_add_from_melon',
)


def album_add_from_melon(request):
    if request.method == 'POST':
        album_id = request.POST['album_id']
        Album.objects.update_or_create_from_melon(album_id)

        return redirect('album:album-list')

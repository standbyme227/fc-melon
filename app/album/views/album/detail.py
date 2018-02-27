from django.shortcuts import render
from ...models import Album

__all__ = (
    'album_detail',
)


def album_detail(request, album_pk):
    context = {
        'album': Album.objects.get(pk=album_pk),
    }
    return render(
        request,
        'album/album_detail.html',
        context,
    )

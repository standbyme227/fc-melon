from django.shortcuts import redirect

from ...models import Artist

__all__ = (
    'artist_delete',
)

def artist_delete(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    artist.delete()
    return redirect('artist:artist-list')

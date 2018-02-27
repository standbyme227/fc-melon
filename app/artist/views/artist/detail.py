from django.shortcuts import render

from ...models import Artist

__all__ = (
    'artist_detail',
)

def artist_detail(request, artist_pk):
    # artist = get_object_or_404
    context = {
        'artist': Artist.objects.get(pk=artist_pk),
    }
    return render(
        request,
        'artist/artist_detail.html',
        context,
    )


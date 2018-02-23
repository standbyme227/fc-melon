from django.shortcuts import render

from ...models import Artist



__all__ = (
    'artist_list',
)


def artist_list(request):
    artists = Artist.objects.all().order_by('pk')
    context = {
        'artists': artists,
    }
    return render(
        request,
        'artist/artist_list.html',
        context,
    )
from django.shortcuts import render

from ...models import Song

__all__ = (
    'song_detail',
)

def song_detail(request, song_pk):
    # artist = get_object_or_404
    context = {
        'song': Song.objects.get(pk=song_pk),
    }
    return render(
        request,
        'song/song_detail.html',
        context,
    )


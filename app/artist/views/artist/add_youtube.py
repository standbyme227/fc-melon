from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from ...models import ArtistYouTube
from ...models import Artist


__all__ = (
    'artist_add_youtube',
)

def artist_add_youtube(request, artist_pk):

    artist = get_object_or_404(Artist, pk=artist_pk)
    artist.youtube_videos.update_or_create(
        youtube_id=request.POST['youtube_id'],
        defaults={
            'title':request.POST['title'],
            'url_thumbnail' : request.POST['thumbnails'],
        }
    )
    next_path = request.POST.get(
        'next-path',
        reverse('artist:artist-detail', kwargs={'artist_pk': artist_pk}),
    )
    # return redirect('artist:artist-detail', artist_pk=artist_pk)
    return redirect(next_path)
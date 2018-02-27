import datetime
from django.shortcuts import render, redirect, get_object_or_404
from ...models import Artist
from ...forms import ArtistForm

__all__ = (
    'artist_edit',
)


def artist_edit(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist:artist-list')
    else:
        form = ArtistForm(instance=artist)
    context = {
        'artist_form': form,
    }
    return render(request, 'artist/artist_edit.html', context)



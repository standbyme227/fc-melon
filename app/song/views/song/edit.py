import datetime
from django.shortcuts import render, redirect, get_object_or_404
from ...models import Song
from ...forms import SongForm

__all__ = (
    'song_edit',
)


def song_edit(request, song_pk):
    song = get_object_or_404(Song, pk=song_pk)
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song:song-list')
    else:
        form = SongForm(instance=song)
    context = {
        'song_form': form,
    }
    return render(request, 'song/song_edit.html', context)



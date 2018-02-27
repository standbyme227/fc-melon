import datetime
from django.shortcuts import render, redirect
from ...models import Song
from ...forms import SongForm


__all__ = (
    'song_add',
)

def song_add(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song:song-list')
    else:
        form = SongForm()
    context = {
        'song_form': form,
    }
    return render(request, 'song/song_add.html', context)

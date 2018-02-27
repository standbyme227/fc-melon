import datetime
from django.shortcuts import render, redirect
from ...models import Album
from ...forms import AlbumForm

__all__ = (
    'album_add',
)

def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album:album-list')
    else:
        form = AlbumForm()
    context = {
        'album_form' : form,
    }
    return render(request, 'album/album_add.html', context)




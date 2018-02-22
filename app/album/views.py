from django.shortcuts import render

from album.models import Album


def album_list(request):

    albums = Album.objects.all() #.order_by('-pk')
    context = {
        'albums': albums,
    }
    return render(request, 'album/album_list.html', context,)
from django.shortcuts import render

from song.models import Song


def song_list(request):

    songs = Song.objects.all() #.order_by('-pk')
    context = {
        'songs': songs,
    }
    return render(request, 'song/song_list.html', context)

def song_search(request):

    # songs = Song.objects.get()

    return render(request, 'song/song_search.html')
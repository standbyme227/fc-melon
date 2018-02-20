from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from song.models import Song


def song_list(request):

    songs = Song.objects.all() #.order_by('-pk')
    context = {
        'songs': songs,
    }
    return render(request, 'song/song_list.html', context)

def song_search(request):


    context = {}
    # songs = Song.objects.get()
    if request.method == 'POST':
        keyword = request.POST['keyword'].strip()
        if keyword:
            songs_from_artists = Song.objects.filter(album__artists__name__contains=keyword).distinct()
            songs_from_albums = Song.objects.filter(album__title__contains=keyword).distinct()
            songs_from_titles = Song.objects.filter(title__contains=keyword).distinct()
            context['songs_from_albums'] = songs_from_albums
            context['songs_from_artist'] = songs_from_artists
            context['songs_from_title'] = songs_from_titles
    # 만약 method 가 POST였다면 context에 'songs'가 채워진 상태,
    # GET이면 빈 상태로 render 실행
    return render(request, 'song/song_search.html', context)




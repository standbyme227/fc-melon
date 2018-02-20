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

    keyword = request.GET.get('keyword')


    if keyword:
        # Song목록 중 title이 keyword를 포함하는 쿼리셋
        songs = Song.objects.filter(
            Q(album__title__contains=keyword) |
            Q(album__artists__name__contains=keyword) |
            Q(title__contains=keyword)
        ).distinct()
        # 미리 선언한 context의 'songs'키에 QuerySet을 할당
        context['songs'] = songs

        # Song과 연결된 Artist의 name에 keyword가 포함되는 경우
        songs_from_artists = Song.objects.filter(
            album__artists__name__contains=keyword
        )
        context['songs_from_artists'] = songs_from_artists

        # Song과 연결된 Album의 title에 keyword가 포함되는 경우
        songs_from_albums = Song.objects.filter(album__title__contains=keyword)
        context['songs_from_albums'] = songs_from_albums

        # Song의 title에 keyword가 포함되는 경우
        songs_from_title = Song.objects.filter(title__contains=keyword)
        context['songs_from_title'] = songs_from_title
        # 만약 method가 POST였다면 context에 'songs'가 채워진 상태,
        # GET이면 빈 상태로 render실행
    return render(request, 'song/song_search.html', context)


    # if keyword:
    #     songs_from_artists = Song.objects.filter(album__artists__name__contains=keyword).distinct()
    #     songs_from_albums = Song.objects.filter(album__title__contains=keyword).distinct()
    #     songs_from_titles = Song.objects.filter(title__contains=keyword).distinct()
    #     context['songs_from_albums'] = songs_from_albums
    #     context['songs_from_artists'] = songs_from_artists
    #     context['songs_from_titles'] = songs_from_titles
    # # 만약 method 가 POST였다면 context에 'songs'가 채워진 상태,
    # # GET이면 빈 상태로 render 실행
    #     return render(request, 'song/song_search.html', context)
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
            songs = Song.objects.filter(title__contains=keyword)
            context['songs'] = songs
    # 만약 method 가 POST였다면 context에 'songs'가 채워진 상태,
    # GET이면 빈 상태로 render 실행
    return render(request, 'song/song_search.html', context)




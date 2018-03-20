from collections import namedtuple
from typing import NamedTuple

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from ...models import Song

__all__ = (
    'song_search',
)


def song_search(request):
    # songs = Song.objects.get()

    # keyword = request.GET.get('keyword')

    context = {
        'song_infos': [],
    }
    keyword = request.GET.get('keyword')

    # SongInfo = collections.namedtuple('SongInfo', ['type', 'q']) 원래의 namedtuple
    class SongInfo(NamedTuple):
        type: str
        q: Q

    if keyword:
        song_infos = (
            SongInfo(
                type='아티스트명',
                q=Q(album__artists__name__contains=keyword)),
            # Q는 조건이다. 근데 잘 모르겠다.
            SongInfo(
                type='앨범명',
                q=Q(album__title__contains=keyword)),
            SongInfo(
                type='노래제목',
                q=Q(title__contains=keyword)),
        )
        # 위의 튜플에 넣어서 언패킹

        for type, q in song_infos:
            context['song_infos'].append({
                'type': type,
                'songs': Song.objects.filter(q),
            })

    context['type'] = 'ASDF'
    return render(request, 'song/song_search.html', context)

    # # Song목록 중 title이 keyword를 포함하는 쿼리셋
    # songs = Song.objects.filter(
    #     Q(album__title__contains=keyword) |
    #     Q(album__artists__name__contains=keyword) |
    #     Q(title__contains=keyword)
    # ).distinct()
    # # 미리 선언한 context의 'songs'키에 QuerySet을 할당
    # context['songs'] = songs

    # songs_from_artists = Song.objects.filter(album__artists__name__contains=keyword)
    # songs_from_albums = Song.objects.filter(album__title__contains=keyword)
    # songs_from_title = Song.objects.filter(title__contains=keyword)

    # for type, songs in zip(
    #         ('아티스트명', '앨범명', '노래제목'),
    #         (songs_from_artists, songs_from_albums, songs_from_title)):
    #     context['song_infos'].append({
    #         'type':type,
    #         'songs':songs,
    #     })

    # context['song_infos'].append({
    #     'type': '아티스트명',
    #     'songs': songs_from_artists,
    # })
    # context['song_infos'].append({
    #     'type': '앨범명',
    #     'songs': songs_from_albums,
    # })
    # context['song_infos'].append({
    #     'type': '노래제목',
    #     'songs': songs_from_title,
    # })

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

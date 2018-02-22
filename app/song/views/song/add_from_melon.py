from datetime import datetime
import re

from bs4 import BeautifulSoup, NavigableString
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests
from io import BytesIO

from ...models import Song
from ...models import Album

def song_add_from_melon(request):

    if request.method == 'POST' :
        song_id = request.POST['song_id']

        url = f'https://www.melon.com/song/detail.htm'
        params = {
            'songId': song_id,
        }
        response = requests.get(url, params)
        source = response.text


        soup = BeautifulSoup(source, 'lxml')
        # div.song_name의 자식 strong요소의 바로 다음 형제요소의 값을 양쪽 여백을 모두 잘라낸다
        # 아래의 HTML과 같은 구조
        # <div class="song_name">
        #   <strong>곡명</strong>
        #
        #              Heart Shaker
        # </div>
        div_entry = soup.find('div', class_='entry')
        title = div_entry.find('div', class_='song_name').strong.next_sibling.strip()
        artist = div_entry.find('div', class_='artist').get_text(strip=True)
        dl = div_entry.find('div', class_='meta').find('dl')

        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        album_id_link = dl.find('a').get('href')
        album_id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
        album_id = re.search(album_id_pattern,album_id_link).group(1)

        # div_prdcr = soup.find('div', class_='section_prdcr')
        # ul = div_prdcr.find('ul', class_='list_person clfix')
        # items = [item.get_text(strip=True) for item in ul.contents if not isinstance(item, str)]
        # it = iter(items.reverse())
        # unordered_dict = dict(zip(it, it))
        #
        # _producers = unordered_dict

        album_title = description_dict.get('앨범')
        # release_date = description_dict.get('발매일')
        genre = description_dict.get('장르')

        div_lyrics = soup.find('div', id='d_video_summary')

        lyrics_list = []
        for item in div_lyrics:
            if item.name == 'br':
                lyrics_list.append('\n')
            elif type(item) is NavigableString:
                lyrics_list.append(item.strip())
        lyrics = ''.join(lyrics_list)

        album, album_created = Album.objects.get_or_create(melon_album_id=album_id)
        album.title = album_title
        album.save()

        song, song_created = Song.objects.get_or_create(melon_song_id=song_id)

        song.title = title
        song.artist = artist
        song.album = album
        song.lyrics = lyrics
        song.genre = genre
        song.save()



    # 템플릿에 인풋있음. 그거 누르면 리스트가 뜨는데 그 리스트는 멜론 검색리스트 중 곡
    # 그 곡 옆에 버튼이있음 그거 누르면 노래가 추가됨.
    # 아티스트가 추가되려면 상세페이지로 가는 url에서 노래에 맞는 id값이 필요할테고
    # 그걸 첫 크롤링 그니까 리스트를 뽑아올때 얻어야한다.

        return redirect('song:song-list')
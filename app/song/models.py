from django.conf import settings
from django.db import models
from album.models import Album
from artist.models import Artist
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString
from pip._vendor import requests
import re
from django.utils import timezone


class SongManager(models.Manager):
    def update_or_create_from_melon(self, song_id):
        '''
        song_id에 해당하는 Song정보를 멜론 사이트에서 가져와 update_or_create를 실행
        이 때, 해당 Song의 Artist정보도 가져와 ArtistManager.update_or_create_from_melon도 실행
        :param song_id: 멜론 사이트에서의 곡 고유 ID
        :return: (Song instance, Bool(Song created))
        '''
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
        artist_name = div_entry.find('div', class_='artist').get_text(strip=True)
        dl = div_entry.find('div', class_='meta').find('dl')

        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        artist_id_link = div_entry.find('div', class_='artist').find('a').get('href')
        artist_id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
        artist_id = re.search(artist_id_pattern, artist_id_link).group(1)

        album_id_link = dl.find('a').get('href')
        album_id_pattern = re.compile(r'.*?(\d+).*?', re.DOTALL)
        album_id = re.search(album_id_pattern, album_id_link).group(1)

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

        lyrics = ''
        # 가사는 기본적으로 빈 문자열로 지정한 뒤
        if div_lyrics:
            lyrics_list = []
            for item in div_lyrics:
                if item.name == 'br':
                    lyrics_list.append('\n')
                elif type(item) is NavigableString:
                    lyrics_list.append(item.strip())
            lyrics = ''.join(lyrics_list)
        # 있다면 join으로 채워넣는 방식으로 구현한다.
        # 왜냐면 lyrics가 없는 경우가 있기때문에

        album, album_created = Album.objects.update_or_create_from_melon(album_id)

        artist, artist_created = Artist.objects.update_or_create_from_melon(artist_id)

        song, song_created = Song.objects.update_or_create(
            melon_song_id=song_id,
            defaults={
                'title': title,
                'album': album,
                'lyrics': lyrics,
                'genre': genre,
            }
        )
        song.artists.add(artist)

        return song, song_created


class Song(models.Model):
    melon_song_id = models.CharField('멜론 Song ID', max_length=20, blank=True, null=True, unique=True)
    title = models.CharField('곡 제목', max_length=50)
    genre = models.CharField('장르', max_length=100, blank=True)
    lyrics = models.TextField('가사', blank=True)
    album = models.ForeignKey(Album, verbose_name='앨범', on_delete=models.CASCADE, blank=True, null=True)
    artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록', blank=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # 이게 유저를 settings에서 불러온거다.
        through='SongLike',  # MTM의 중개모델이 뭔지를 지정
        related_name='like_songs',  # related_manager의 이름을 지정한다.
        blank=True,
    )

    @property
    def release_date(self):
        return self.album.release_date

    @property
    def formatted_release_date(self):
        return self.release_date.strftime('%Y.%m.%d')

    objects = SongManager()

    # through????
    # artist와 song의 다대다관계를 ArtistSong 이라는 클래스를 통해서 만들겠다??

    def __str__(self):
        # if self.album:
        #     return '{artists} - {title} ({album})'.format(
        #         artists=', '.join(self.album.artists.values_list('name', flat=True)),
        #         title = self.title,
        #         album = self.album.title
        #     )
        return self.title

        # 불러오는건 album이었지만 album에 str부분이 title이라서 이렇게 나온거 같다.

    def toggle_like_user(self, user):
        # 자신이 'artist이며 user가 주어진 user인 ArtistLike를 가져오거나 없으면 생성
        like, like_created = self.like_user_info_list.get_or_create(user=user)
        # 만약 이미 잇엇을 경우 (새로 생성 X)
        if not like_created:
            # Like를 지워줌
            like.delete()
        # 생성여부를 반환
        return like_created


class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    demo_date = models.DateTimeField(blank=True, null=True)

    # producer = models.ForeignKey()

    def __str__(self):
        pass


class SongLike(models.Model):
    song = models.ForeignKey(Song, related_name='like_user_info_list', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like_song_info_list', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{song}을 좋아합니다. -{user}, {date}-'.format(
            song=self.song.title,
            user=self.user.username,
            date=datetime.strftime(
                timezone.localtime(self.created_date),
                '%Y.%m.%d')
        )

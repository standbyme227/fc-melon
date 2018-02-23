import re

from artist.models import Artist
from datetime import datetime
from bs4 import BeautifulSoup
from pip._vendor import requests
from django.db import models
from io import BytesIO
from django.core.files import File
from pathlib import Path
from django.http import HttpResponse
from utils.file import *


class AlbumManager(models.Manager):
    def update_or_create_from_melon(self, album_id):
        url = f'https://www.melon.com/album/detail.htm'
        params = {
            'albumId': album_id,
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')

        div_info = soup.find('div', class_='wrap_info')
        div_thumb = soup.find('div', class_='thumb')

        dl = div_info.find('div', class_='entry').find('div', class_='meta').find('dl', class_='list')

        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        # album_id =
        album_title = div_info.find('div', class_='song_name').strong.next_sibling.strip()
        url_img_cover = div_thumb.find('a', id='d_album_org').find('img').get('src')

        # url_img_cover_pattern = re.compile(r'(.*?.jpg)/melon.*?', re.DOTALL)
        # url_img_cover = re.search(url_img_cover_pattern, url_img_cover_link)

        release_date = description_dict.get('발매일')

        # response = requests.get(url_img_cover)
        # # url_img_cover는 이미지의 URL
        # binary_data = response.content
        # # requests에 GET요청을 보낸 결과의 Binary data
        # temp_file = BytesIO()
        # # 파일 처럼 취급되는 메모리 객체 temp_file을 생성
        # temp_file.write(binary_data)
        # # temp_file에 이진데이터를 기록
        # temp_file.seek(0)
        # # 파일객체의 포인터를 시작부분으로 되돌렸는데 패치되서 없어도됨

        album, album_created = self.update_or_create(
            melon_album_id=album_id,
            defaults={
                'title': album_title,
                'release_date': datetime.strptime(
                    release_date, '%Y.%m.%d') if release_date else None,
            }
        )

        temp_file = download(url_img_cover)
        file_name = '{album_id}.{ext}'.format(
            album_id=album_id,
            ext=get_buffer_ext(temp_file),
        )

        album.img_cover.save(file_name, File(temp_file))
        return album, album_created


class Album(models.Model):
    melon_album_id = models.CharField('멜론 Album ID', max_length=20, blank=True, null=True, unique=True)
    title = models.CharField(max_length=255)  # 앨범 제목임~
    img_cover = models.ImageField('커버 이미지', upload_to='album', blank=True)
    # artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록', blank=True)
    #  Album의 artist는 정방향참조 가능... 역참조와 정방향참조는 뭔가???
    release_date = models.DateField(max_length=50, blank=True, null=True)

    # genre = models.CharField(max_length=50, blank=True,)

    # publisher = models.CharField(max_length=50, blank=True,)
    # agency = models.CharField(max_length=50, blank=True,)

    @property
    def genre(self):
        return ', '.join(self.song_set.values_list('genre', flat=True).distinct())

    objects = AlbumManager()

    def __str__(self):
        # return '{title} [{artists}]'.format(
        #     title=self.title,
        #     artists = ', '.join(self.artists.values_list('name', flat=True))
        # )
        return self.title

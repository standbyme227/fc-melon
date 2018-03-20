import re

from artist.models import Artist
from pip._vendor import requests
from io import BytesIO
from django.core.files import File
from pathlib import Path
from django.http import HttpResponse
from datetime import datetime
from bs4 import BeautifulSoup
from django.db import models
from django.conf import settings
from utils.file import *
from .managers import *

__all__ = (
    'Album',
)


class Album(models.Model):
    melon_album_id = models.CharField('멜론 Album ID', max_length=20, blank=True, null=True, unique=True)
    title = models.CharField(max_length=255)  # 앨범 제목임~
    img_cover = models.ImageField('커버 이미지', upload_to='album', blank=True)
    # artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록', blank=True)
    #  Album의 artist는 정방향참조 가능... 역참조와 정방향참조는 뭔가???
    release_date = models.DateField(max_length=50, blank=True, null=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # 이게 유저를 settings에서 불러온거다.
        through='AlbumLike',  # MTM의 중개모델이 뭔지를 지정
        related_name='like_albums',  # related_manager의 이름을 지정한다.
        blank=True,
    )

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

    def toggle_like_user(self, user):
        # 자신이 'artist이며 user가 주어진 user인 ArtistLike를 가져오거나 없으면 생성
        like, like_created = self.like_user_info_list.get_or_create(user=user)
        # 만약 이미 잇엇을 경우 (새로 생성 X)
        if not like_created:
            # Like를 지워줌
            like.delete()
        # 생성여부를 반환
        return like_created

    def to_json(self):
        data = {
            'melon_album_id': self.melon_album_id,
            'title': self.title
        }
        return data

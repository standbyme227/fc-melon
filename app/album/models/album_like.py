from datetime import datetime
from bs4 import BeautifulSoup
from django.db import models
from django.conf import settings
from utils.file import *
from .album import *
from django.utils import timezone

__all__ = (
    'AlbumLike',
)


class AlbumLike(models.Model):
    album = models.ForeignKey(Album, related_name='like_user_info_list', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like_album_info_list', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{song}을 좋아합니다. -{user}, {date}-'.format(
            song=self.album.title,
            user=self.user.username,
            date=datetime.strftime(
                timezone.localtime(self.created_date),
                '%Y.%m.%d')
        )

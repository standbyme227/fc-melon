import re
from datetime import datetime

from bs4 import BeautifulSoup
from django.conf import settings
from pip._vendor import requests
from django.db import models
from io import BytesIO
from django.core.files import File
from pathlib import Path

from members.models import User
from utils.file import *
from django.utils import timezone
from .artist import Artist

__all__ = (
    'ArtistLike',
)




class ArtistLike(models.Model):
    artist = models.ForeignKey(Artist, related_name='like_user_info_list', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like_artist_info_list', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('artist', 'user'),
        )

    def __str__(self):
        return '"{artist}"의 좋아요({username}, {date})'.format(
            artist=self.artist.name,
            username=self.user.username,
            date=datetime.strftime(
                timezone.localtime(self.created_date),
                '%Y.%m.%d')
        )

    # class Meta:
    #     verbose_name_plural = 'intermediate - Postlike'

    # response = requests.get(url_img_cover)
    # binary_data = response.content
    # temp_file = BytesIO()
    # temp_file.write(binary_data)
    # temp_file.seek(0)

    # artist, artist_created = self.get_or_create(melon_id=artist_id)
    #
    # artist.name = name
    # # artist.real_name = real_name
    # artist.nationality = nationality
    # if birth_date_str == None:
    #     pass
    # else:
    #     artist.birth_date = datetime.strptime(birth_date_str, '%Y.%m.%d')
    # artist.constellation = constellation
    # artist.blood_type = blood_type
    # artist.save()
    #
    # return artist, artist_created

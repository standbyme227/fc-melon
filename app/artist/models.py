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


class ArtistManager(models.Manager):
    def update_or_create_from_melon(self, artist_id):

        url = f'https://www.melon.com/artist/detail.htm'
        params = {
            'artistId': artist_id,
        }
        response = requests.get(url, params)

        soup = BeautifulSoup(response.text, 'lxml')

        div_artist_info = soup.find('div', class_='wrap_atist_info')
        div_wrap_thumb = soup.find('div', class_='wrap_thumb')

        dl = div_artist_info.find('dl', class_='atist_info clfix')
        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        section = soup.find('div', class_='section_atistinfo04')
        dl2 = section.find('dl', class_='list_define clfix')
        items = [item.get_text(strip=True) for item in dl2.contents if not isinstance(item, str)]
        it2 = iter(items)
        description_dict2 = dict(zip(it2, it2))

        name = div_artist_info.find('p', class_='title_atist').strong.next_sibling.strip()

        url_img_cover = div_wrap_thumb.find('span', id='artistImgArea').find('img').get('src')
        # url_img_cover_pattern = re.compile(r'(.*?.jpg)/melon.*?', re.DOTALL)
        # url_img_cover = re.search(url_img_cover_pattern, url_img_cover_link).group(1)

        real_name = description_dict2.get('본명')
        nationality = description_dict2.get('국적')
        birth_date_str = description_dict2.get('생일')
        constellation = description_dict2.get('별자리')
        blood_type = description_dict2.get('혈액형')

        # for short, full in Artist.CHOICES_BLOOD_TYPE:
        #     if blood_type == None:
        #         blood_type = Artist.BLOOD_TYPE_OTHER
        #
        #     elif blood_type.strip() == full:
        #         blood_type = short
        #         break
        #     else:
        #         blood_type = Artist.BLOOD_TYPE_OTHER

        for short, full in Artist.CHOICES_BLOOD_TYPE:
            if blood_type == None:
                blood_type = Artist.BLOOD_TYPE_OTHER
            elif blood_type.strip() == full:
                blood_type = short
                break
        else:
            blood_type = Artist.BLOOD_TYPE_OTHER

        artist, artist_created = self.update_or_create(
            melon_id=artist_id,
            defaults={
                'name': name,
                'real_name': real_name if real_name else '',
                'nationality': nationality,
                'birth_date': datetime.strptime(
                    birth_date_str, '%Y.%m.%d') if birth_date_str else None,
                'constellation': constellation,
                'blood_type': blood_type,
            }
        )

        temp_file = download(url_img_cover)
        file_name = '{artist_id}.{ext}'.format(
            artist_id=artist_id,
            ext=get_buffer_ext(temp_file),
        )

        # if artist.image:
        #     artist.image.delete()
        # 아티스트 이미지가 있다면 지운다.
        if not artist.image:
            artist.image.save(file_name, File(temp_file))
        # 아티스트 이미지가 없다면 만든다.
        return artist, artist_created


class Artist(models.Model):
    BLOOD_TYPE_A = 'a'
    BLOOD_TYPE_B = 'b'
    BLOOD_TYPE_O = 'o'
    BLOOD_TYPE_AB = 'c'
    BLOOD_TYPE_OTHER = 'x'
    CHOICES_BLOOD_TYPE = (
        (BLOOD_TYPE_A, 'A형'),
        (BLOOD_TYPE_B, 'B형'),
        (BLOOD_TYPE_O, 'O형'),
        (BLOOD_TYPE_AB, 'AB형'),
        (BLOOD_TYPE_OTHER, '기타'),
    )

    melon_id = models.CharField('멜론 Artist ID', max_length=20, blank=True, null=True, unique=True)
    image = models.ImageField('프로필 이미지', upload_to='artist', blank=True)
    # upload_to는 media폴더를 기준으로 그안의 경로를 지정
    name = models.CharField('이름', max_length=50, )
    real_name = models.CharField('본명', max_length=30, blank=True, default='')
    nationality = models.CharField('국적', max_length=50, blank=True, )
    birth_date = models.DateField(max_length=50, blank=True, null=True, )
    constellation = models.CharField('별자리', max_length=30, blank=True, null=True)
    blood_type = models.CharField('혈액형', max_length=50, blank=True, choices=CHOICES_BLOOD_TYPE)
    # choices를 넣어야지만 위의 선택을 이용할 수 있다.
    intro = models.TextField('소개', blank=True)
    # likes = models.IntegerField(default=0)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='ArtistLike',
        related_name='like_artists',
        blank=True,
    )

    objects = ArtistManager()

    def __str__(self):
        return self.name

    def toggle_like_user(self, user):
        # 자신이 'artist이며 user가 주어진 user인 ArtistLike를 가져오거나 없으면 생성
        like, like_created = self.like_user_info_list.get_or_create(user=user)
        # 만약 이미 잇엇을 경우 (새로 생성 X)
        if not like_created:
            # Like를 지워줌
            like.delete()
        # 생성여부를 반환
        return like_created

        # if self.like_users.filter(user=user).exists():
        #     self.like_users.filter(user).delete()
        # else:
        #     self.like_users.create(user=user)


        # # 자신이 artist이며, 주어진 user와의 ArtistLike의 QuerySet
        # query = ArtistLike.objects.filter(artist=self, user=user)
        # # QuerySet이 존재할 졍우
        # if query.exists():
        #     query.delete()
        #     return False
        # # QuerySet이 존재하지 않을 경우
        # else:
        #     ArtistLike.objects.create(artist=self, user=user)
        #     return True


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

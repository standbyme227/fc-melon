from django.conf import settings
from django.db import models

from .artist_youtube import ArtistYouTube
from .managers import ArtistManager

__all__ = (
    'Artist',
)


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

    youtube_videos = models.ManyToManyField(
        ArtistYouTube,
        related_name='artists',
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

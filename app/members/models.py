from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def toggle_like_artist(self, artist):
        like, like_created = self.like_artist_info_list.get_or_create(artist=artist)
        if not like_created:
            like.delete()
        return like_created
    pass

# DB가 저장될 수 있는 테이블이랄까??????
# django에서 모델이라는 존재는 그런 존재.
# 데이터를 저장하기위한 필드 생성.

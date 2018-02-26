from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

# DB가 저장될 수 있는 테이블이랄까??????
# django에서 모델이라는 존재는 그런 존재.
# 데이터를 저장하기위한 필드 생성.

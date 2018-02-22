from django.db import models


class Artist(models.Model):
    BLOOD_TYPE_A = 'a'
    BLOOD_TYPE_B = 'b'
    BLOOD_TYPE_O = 'o'
    BLOOD_TYPE_C = 'c'
    BLOOD_TYPE_OTHER = 'x'
    CHOICES_BOOD_TYPE = (
        (BLOOD_TYPE_A, 'A형'),
        (BLOOD_TYPE_B, 'B형'),
        (BLOOD_TYPE_O, 'O형'),
        (BLOOD_TYPE_C, 'AB형'),
        (BLOOD_TYPE_OTHER, '기타'),
    )
    melon_id = models.CharField('멜론 Artist ID', max_length=20, blank=True, null=True, unique=True)
    image = models.ImageField('프로필 이미지', upload_to='artist', blank=True )
    # upload_to는 media폴더를 기준으로 그안의 경로를 지정
    name = models.CharField('이름', max_length=50, )
    real_name = models.CharField('본명', max_length=30, blank=True, default='')
    nationality = models.CharField('국적', max_length=50, blank=True, )
    birth_date = models.DateField(max_length=50, blank=True, null=True, )
    constellation = models.CharField('별자리', max_length=30, blank=True, null=True)
    blood_type = models.CharField('혈액형', max_length=50, blank=True,)
    intro = models.TextField('소개', blank=True)

    def __str__(self):
        return self.name


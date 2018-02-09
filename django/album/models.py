from django.db import models
from artist.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=255) # 앨범 제목임~
    img_cover = models.ImageField('커버 이미지', upload_to='album', blank=True)
    artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록')  # Album의 artist는 정방향참조 가능... 역참조와 정방향참조는 뭔가???
    release_date = models.DateField(max_length=50, blank=True, null=True)
    # genre = models.CharField(max_length=50, blank=True,)

    # publisher = models.CharField(max_length=50, blank=True,)
    # agency = models.CharField(max_length=50, blank=True,)

    @property
    def genre(self):
        return  ', '.join(self.song_set.values_list('genre', flat=True).distinct())

    def __str__(self):

        return '{title} [{artists}]'.format(
            title=self.title,
            artists = ', '.join(self.artists.values_list('name', flat=True))
        )





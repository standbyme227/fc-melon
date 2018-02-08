
from django.db import models
from album.models import Album
from artist.models import Artist


class Song(models.Model):
    title = models.CharField('곡 제목', max_length=50)
    genre = models.CharField('장르', max_length=100, blank=True)
    lyrics = models.TextField('가사', blank=True)
    album = models.ForeignKey(Album, verbose_name='앨범', on_delete=models.CASCADE, blank=True, null=True)


    @property
    def artists(self):
        return self.album.artists.all()


    @property
    def release_date(self):
        return self.album.release_date

    @property
    def formatted_release_date(self):
        return self.release_date.strftime('%Y.%m.%d')



    # through????
    # artist와 song의 다대다관계를 ArtistSong 이라는 클래스를 통해서 만들겠다??

    def __str__(self):
        return '{artists} - {title} ({album})'.format(
            artists=', '.join(self.album.artists.values_list('name', flat=True)),
            title = self.title,
            album = self.album.title
        )

        #불러오는건 album이었지만 album에 str부분이 title이라서 이렇게 나온거 같다.

class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    demo_date = models.DateTimeField(blank=True, null=True)
    #producer = models.ForeignKey()

    def __str__(self):
        pass
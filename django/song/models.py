from django.db import models
from album.models import Album
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ManyToManyField(Artist, through="ArtistSong")  # through_fields=('artist','song')
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #앨범을 지우면 함께 지워지게 하기위해서 CASCADE를 지정했다.


    # through????
    # artist와 song의 다대다관계를 ArtistSong 이라는 클래스를 통해서 만들겠다??

    def __str__(self):
        return f'{self.title} - {self.album} 가수 : {self.artist}' #불러오는건 album이었지만 album에 str부분이 title이라서 이렇게 나온거 같다.

class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    demo_date = models.DateTimeField(blank=True, null=True)
    #producer = models.ForeignKey()

    def __str__(self):
        return f'artist: {self.artist} - song : {self.song.title}'
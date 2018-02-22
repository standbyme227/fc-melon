from django.contrib import admin
from .models import Song, ArtistSong

admin.site.register(Song)
admin.site.register(ArtistSong)

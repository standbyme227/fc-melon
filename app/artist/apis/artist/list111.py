from django.http import JsonResponse

from ...models import Artist
from ...models import ArtistManager


def artist_list(request):
    artists = Artist.objects.all()

    data = {
        'artists': [artist.to_json() for artist in artists],
    }

    # data = {
    #     'artists': list(artists.values())
    # }
    # data = {
    #     'artists': list(artists.values())
    # }
    # 특정값이 피요하다면 values()안에 pk나 name등을 명시하면된다.

    return JsonResponse(data)

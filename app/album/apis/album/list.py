import json

from django.http import JsonResponse, HttpResponse
from ...models import Album
__all__ = (
    'album_list',
)
def album_list(request):

    albums = Album.objects.all()

    # data = {
    #     'albums': [ {'melon_album_id': album.melon_album_id, 'title': album.title} for album in albums ]
    # }

    data = {
        'albums': [album.to_json() for album in albums ]
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    # 같다.
    return JsonResponse(data)
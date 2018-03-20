from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ...permissions import IsOwnerOrReadOnly
from utils.paginations import StandardResultsSetPagination
from ...models import Artist
from ...serializers import ArtistSerializer

__all__ = (
    'ArtistList',
    'ArtistDetail',
)


# class ArtistListView(APIView):
#
#     def get(self, request):
#         artists = Artist.objects.all()
#         serializer = ArtistSerializer(artists, many=True)
#         return Response(serializer.data)


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        print('request.user:', request.user)
    #     return self.list(request, *args, **kwargs)
        return super().get(request,*args, **kwargs)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    pagination_class = StandardResultsSetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )



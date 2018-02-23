from datetime import datetime
import re

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests
from io import BytesIO

from ...models import Artist


def artist_add_from_melon(request):
    if request.method == 'POST':
        artist_id = request.POST['artist_id']
        Artist.objects.update_or_create_from_melon(artist_id)
        return redirect('artist:artist-list')

        # Artist.objects.update_or_create(
        #     melon_id = artist_id,
        #     defaults={
        #         'name': name,
        #         'real_name': real_name,
        #         'nationality' : nationality,
        #         'birth_date' : datetime.strptime(birth_date_str, '%Y.%m.%d'),
        #         'constellation' : constellation,
        #         'blood_type' : blood_type,
        #     }
        # )

        # # return HttpResponse(birth_date_str)
        # if not artist_id == Artist.objects.filter(melon_id=artist_id):
        #     Artist.objects.create(
        #         melon_id=artist_id,
        #         name=name,
        #         real_name=real_name,
        #         nationality=nationality,
        #         birth_date_str=datetime.strptime(birth_date_str, '%Y.%m.%d'),
        #         constellation=constellation,
        #         blood_type=blood_type,
        #     )

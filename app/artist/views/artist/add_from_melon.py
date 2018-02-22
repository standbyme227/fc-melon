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
        url = f'https://www.melon.com/artist/detail.htm'
        params = {
            'artistId': request.POST['artist_id'],
        }
        response = requests.get(url, params)

        soup = BeautifulSoup(response.text, 'lxml')

        div_artist_info = soup.find('div', class_='wrap_atist_info')
        div_wrap_thumb = soup.find('div', class_='wrap_thumb')

        dl = div_artist_info.find('dl', class_='atist_info clfix')
        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        section = soup.find('div', class_='section_atistinfo04')
        dl2 = section.find('dl', class_='list_define clfix')
        items = [item.get_text(strip=True) for item in dl2.contents if not isinstance(item, str)]
        it2 = iter(items)
        description_dict2 = dict(zip(it2, it2))

        name = div_artist_info.find('p', class_='title_atist').strong.next_sibling.strip()
        url_img_cover = div_wrap_thumb.find('span', id='artistImgArea').find('img').get('src')
        real_name = description_dict2.get('본명')
        nationality = description_dict2.get('국적')
        birth_date_str = description_dict2.get('생일')
        constellation = description_dict2.get('별자리')
        blood_type = description_dict2.get('혈액형')



        for short, full in Artist.CHOICES_BOOD_TYPE:
            if blood_type == None:
                blood_type = Artist.BLOOD_TYPE_OTHER

            elif blood_type.strip() == full:
                blood_type = short
                break
            else:
                blood_type = Artist.BLOOD_TYPE_OTHER

        # response = requests.get(url_img_cover)
        # binary_data = response.content
        # temp_file = BytesIO()
        # temp_file.write(binary_data)
        # temp_file.seek(0)






        artist, artist_created = Artist.objects.get_or_create(melon_id=artist_id)

        artist.name = name
        artist.real_name = real_name
        artist.nationality = nationality
        if birth_date_str == None:
            pass
        else:
            artist.birth_date = datetime.strptime(birth_date_str, '%Y.%m.%d')
        artist.constellation = constellation
        artist.blood_type = blood_type
        artist.save()



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

        return redirect('artist:artist-list')


        # from pathlib import Path
        # file_name = Path(url_img_cover).name
        # artist.img_profile.save(file_name, File(temp_file))
        # return redirect('artist:artist-list')




    def song_add_from_melon(request):

        pass
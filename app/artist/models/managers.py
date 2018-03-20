from datetime import datetime
from bs4 import BeautifulSoup
from django.db import models
from utils.file import *

__all__ = (
    'ArtistManager',
)


class ArtistManager(models.Manager):

    def to_dict(self):
        result = []
        for instance in  self.get_queryset():
            result.append(instance.to_json())
        return result


    def update_or_create_from_melon(self, artist_id):

        from .artist import Artist

        url = f'https://www.melon.com/artist/detail.htm'
        params = {
            'artistId': artist_id,
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
        # url_img_cover_pattern = re.compile(r'(.*?.jpg)/melon.*?', re.DOTALL)
        # url_img_cover = re.search(url_img_cover_pattern, url_img_cover_link).group(1)

        real_name = description_dict2.get('본명')
        nationality = description_dict2.get('국적')
        birth_date_str = description_dict2.get('생일')
        constellation = description_dict2.get('별자리')
        blood_type = description_dict2.get('혈액형')

        # for short, full in Artist.CHOICES_BLOOD_TYPE:
        #     if blood_type == None:
        #         blood_type = Artist.BLOOD_TYPE_OTHER
        #
        #     elif blood_type.strip() == full:
        #         blood_type = short
        #         break
        #     else:
        #         blood_type = Artist.BLOOD_TYPE_OTHER

        for short, full in Artist.CHOICES_BLOOD_TYPE:
            if blood_type == None:
                blood_type = Artist.BLOOD_TYPE_OTHER
            elif blood_type.strip() == full:
                blood_type = short
                break
        else:
            blood_type = Artist.BLOOD_TYPE_OTHER

        artist, artist_created = self.update_or_create(
            melon_id=artist_id,
            defaults={
                'name': name,
                'real_name': real_name if real_name else '',
                'nationality': nationality,
                'birth_date': datetime.strptime(
                    birth_date_str, '%Y.%m.%d') if birth_date_str else None,
                'constellation': constellation,
                'blood_type': blood_type,
            }
        )

        temp_file = download(url_img_cover)
        file_name = '{artist_id}.{ext}'.format(
            artist_id=artist_id,
            ext=get_buffer_ext(temp_file),
        )

        # if artist.image:
        #     artist.image.delete()
        # 아티스트 이미지가 있다면 지운다.
        if not artist.image:
            artist.image.save(file_name, File(temp_file))
        # 아티스트 이미지가 없다면 만든다.
        return artist, artist_created

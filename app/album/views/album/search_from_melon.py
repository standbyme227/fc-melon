import re

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor import requests
from django.contrib.auth import authenticate

from album.models import Album

__all__ = (
    'album_search_from_melon',
)


def album_search_from_melon(request):
    context = {'album_info_list': []}

    keyword = request.GET.get('keyword')

    if keyword:

        url = 'https://www.melon.com/search/album/index.htm'
        params = {
            'q': keyword,
        }

        response = requests.get(url, params)

        print(response)

        soup = BeautifulSoup(response.text, 'lxml')

        album_info_list = []

        for li in soup.select('form#frm div > ul.album11_ul > li'):
            dl = li.select_one('div.atist_info > dl')
            href = li.select_one('a.thumb').get('href')
            p = re.compile(r"goAlbumDetail\('(\d+)'\)")

            title = dl.select_one('dt:nth-of-type(1) > a').get_text(strip=True)
            img_cover = li.select_one('a.thumb img').get('src')
            album_id = re.search(p, href).group(1)

            album_info_list.append({
                'title': title,
                'img_cover': img_cover,
                'album_id': album_id,
                'is_exist': Album.objects.filter(melon_album_id=album_id).exists(),
            })

        context['album_info_list'] = album_info_list
    return render(request, 'album/album_search_from_melon.html', context)

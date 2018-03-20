from datetime import datetime
import re

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.core.files import File
from django.shortcuts import render, redirect
from pip._vendor import requests
from io import BytesIO

__all__ = (
    'song_search_from_melon',
)


def song_search_from_melon(request):
    context = {'songs_info_list': []}

    keyword = request.GET.get('keyword')

    if keyword:

        url = 'https://www.melon.com/search/song/index.htm'
        params = {
            'q': keyword,
        }

        response = requests.get(url, params)

        print(response)

        soup = BeautifulSoup(response.text, 'lxml')
        # 뷰티풀숲을 이용해서 response의 text형식을 lxml로 읽고 soup이라는 변수에 할당
        tr_list = soup.select('form#frm_defaultList table > tbody > tr')
        # frm)defaultList라는 아이디를 가지고 있는 form안에 table 안에 tbody 안에 tr을 이용해서 tr리스트를 만든다
        # 위의 공식과 아래 공식은 같은 효과를 지닌다.
        # tr_list = soup.find('form', id = 'frm_defaultList').find('table').find('tbody').find('tr')

        song_info_list = []
        # result라는 빈리스트를 생성
        for tr in tr_list:
            song_id = tr.select_one('td:nth-of-type(1) input[type=checkbox]').get('value')
            if tr.select_one('td:nth-of-type(3) a.fc_gray'):
                title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
            else:
                title = tr.select_one('td:nth-of-type(3) > div > div > span').get_text(strip=True)
            artist = tr.select_one('td:nth-of-type(4) span.checkEllipsisSongdefaultList').get_text(
                strip=True)
            album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

            song_info_list.append({
                'song_id': song_id,
                'title': title,
                'artist': artist,
                'album': album,
            })

        context['song_info_list'] = song_info_list

    return render(request, 'song/song_search_from_melon.html', context)
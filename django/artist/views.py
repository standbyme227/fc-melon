import datetime

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor import requests

from artist.models import Artist


def artist_list(request):

    artists = Artist.objects.all() #.order_by('-pk')
    context = {
        'artists': artists,
    }
    return render(request, 'artist/artist_list.html', context)


def artist_add(request):

    if request.method == 'POST':
        name = request.POST['name']
        real_name = request.POST['real-name']
        nationality = request.POST['nationality']
        birth_date = request.POST['birth-date']
        constellation = request.POST['constellation']
        blood_type = request.POST['blood-type']
        intro = request.POST['intro']

        Artist.objects.create(
            name=name,
            real_name=real_name,
            nationality=nationality,
            birth_date=datetime.datetime.strptime(birth_date,'%Y-%m-%d'),
            constellation=constellation,
            blood_type=blood_type,
            intro=intro
            )
        return redirect('artist:artist-list' )
    elif request.method == 'GET':
    # elif request.method == 'GET':
    #     pass
        return render(request, 'artist/artist_add.html')

def artist_add_from_melon(request):

    context = {
        'artist_info_list': [],
    }

    keyword = request.GET.get('keyword')
    if keyword:
        url = 'https://www.melon.com/search/artist/index.htm'
        params = {
            'q': keyword
        }

        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        li_list = soup.select('div#pagelist  ul  li')

        # 구분을 그냥 텍스트로 받는다
        # 장르는 리스트로 받는다.
        # 이름, 구분, 장르, 대표곡을 받는다.

        result = []
        for li in li_list:
            artist_id = li.select_one('div.artist_info input[type=hidden]').get('value')
            name = li.select_one('div.artist_info a.ellipsis > b').get_text(strip=True)
            types = li.select_one('div.artist_info dd.gubun').get_text(strip=True)

            genre = li.find('dd', class_='fc_strong').find('div').get_text(strip=True)
            repsong = li.find('dd', class_='btn_play').find('a').find('span', class_='songname12').get_text(strip=True)
            # artist = Artist(artist_id=artist_id, name=name, types=types, genre=genre, repsong=repsong)
            result.append({
                artist_id:artist_id
            })

    return render(request, 'artist/artist_add_from_melon.html', context)

#
# def post_detail(request, pk):
#     context= {
#         'post': Post.objects.get(pk=pk),
#     }
#     return render(request, 'blog/post_detail.html', context)
#
#
# def post_add(request):
#     context = { }
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#
#         if not title and content:
#
#             post = Post.objects.create(
#                 author=request.user,
#                 title=title,
#                 content=content
#             )
#
#
#             return redirect('post-detail', pk=post.pk)
#         context['form_error'] = '제목과 내용을 입력해주세요'
#     return render(request, 'blog/post_add_edit.html', context)






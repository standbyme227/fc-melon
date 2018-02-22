import re

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor import requests


def artist_search_from_melon(request):
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

        artist_info_list = []

        for li in soup.select('div.list_atist12.d_artist_list > ul > li'):
            dl = li.select_one('div.atist_info > dl')
            href = li.select_one('a.thumb').get('href')
            p = re.compile(r"goArtistDetail\('(\d+)'\)")

            name = dl.select_one('dt:nth-of-type(1) > a').get_text(strip=True)
            url_img_cover = li.select_one('a.thumb img').get('src')
            artist_id = re.search(p, href).group(1)

            artist_info_list.append({
                'name': name,
                'url_img_cover': url_img_cover,
                'artist_id': artist_id,
            })

        context['artist_info_list'] = artist_info_list
    return render(request, 'artist/artist_search_from_melon.html', context)

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

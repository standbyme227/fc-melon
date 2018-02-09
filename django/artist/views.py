from django.http import HttpResponse
from django.shortcuts import render, redirect
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

        Artist.objects.create(
            name=name
            )
        return redirect('artist:artist-list' )

    # elif request.method == 'GET':
    #     pass
    return render(request, 'artist/artist_add.html')




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






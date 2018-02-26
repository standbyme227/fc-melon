import datetime
from django.shortcuts import render, redirect
from ...models import Artist
from ...forms import ArtistForm

def artist_add(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     real_name = request.POST['real-name']
    #     nationality = request.POST['nationality']
    #     birth_date = request.POST['birth-date']
    #     constellation = request.POST['constellation']
    #     blood_type = request.POST['blood-type']
    #     intro = request.POST['intro']
    #
    #     Artist.objects.create(
    #         name=name,
    #         real_name=real_name,
    #         nationality=nationality,
    #         birth_date=datetime.datetime.strptime(birth_date, '%Y-%m-%d'),
    #         constellation=constellation,
    #         blood_type=blood_type,
    #         intro=intro
    #     )
    #     return redirect('artist:artist-list')
    # elif request.method == 'GET':
    #     # elif request.method == 'GET':
    #     #     pass
    #     return render(request, 'artist/artist_add.html')



    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # melon_id = form.cleaned_data['melon_id']
            # name = form.cleaned_data['name']
            # real_name = form.cleaned_data['real_name']
            # birth_date = form.cleaned_data['birth_date']
            # blood_type = form.cleaned_data['blood_type']
            # Artist.objects.create(
            #     melon_id=melon_id,
            #     name=name,
            #     real_name=real_name,
            #     birth_date=datetime.datetime.strptime(birth_date, '%Y-%m-%d'),
            #     blood_type=blood_type,
            #     )
            #
            return redirect('artist:artist-list')
    else:
        form = ArtistForm()
    context = {
        'artist_form': form,
    }
    return render(request, 'artist/artist_add.html', context)
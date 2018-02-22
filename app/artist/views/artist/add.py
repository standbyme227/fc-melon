import datetime
from django.shortcuts import render, redirect
from ...models import Artist


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
            birth_date=datetime.datetime.strptime(birth_date, '%Y-%m-%d'),
            constellation=constellation,
            blood_type=blood_type,
            intro=intro
        )
        return redirect('artist:artist-list')
    elif request.method == 'GET':
        # elif request.method == 'GET':
        #     pass
        return render(request, 'artist/artist_add.html')

from django.shortcuts import render
from album.models import Album

def home(request):
    data = Album.objects.all()
    print(data)
    # for i in data:
    #     print(i.album_name)
    #     print(i.release_date)
    #     print(i.musician)
    #     print(i.rating)
    #     print()
    return render(request, 'home.html', {'data': data})
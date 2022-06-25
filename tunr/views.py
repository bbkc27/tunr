from django.shortcuts import render, redirect
from .models import Artist, Song
from .forms import ArtistForm, SongForm
from django.http import JsonResponse
from rest_framework import generics
from .serializers import ArtistSerializer, SongSerializer

# Create your views here.

#drf stuff
class ArtistList(generics.ListCreateAPIView):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

class SongList(generics.ListCreateAPIView):
  queryset = Song.objects.all()
  serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Song.objects.all()
  serializer_class = SongSerializer



#old stuff
def artist_list(request):
  artists = Artist.objects.all()
  values_artists = artists.values('name', 'nationality', )
  list_artists = list(values_artists)
 
  # print(type(artists))
  # print(type(values_artists))
  # print(type(list_artists))

  return JsonResponse(list_artists, safe=False)
  # return render(request, 'tunr/artist_list.html', {'artists': artists})

def song_list(request):
  songs = Song.objects.all()
  return render(request, 'tunr/song_list.html', {'songs': songs})

def artist_detail(request, pk):
  artist = Artist.objects.get(id=pk)
  return render(request, 'tunr/artist_detail.html', {'artist': artist})

def song_detail(request, pk):
  song = Song.objects.get(id=pk)
  return render(request, 'tunr/song_detail.html', {'song': song})




def artist_create(request):
  if request.method == 'POST':
    form = ArtistForm(request.POST)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm()
  return render(request, 'tunr/artist_form.html', {'form': form})

def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'tunr/artist_form.html', {'form': form})

def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')

def song_create(request):
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save()
      return redirect('song_list')
  else:
    form = SongForm()
  return render(request, 'tunr/song_form.html', {'form': form})

def song_edit(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'tunr/song_form.html', {'form': form})

def song_delete(request, pk):
    Song.objects.get(id=pk).delete()
    return redirect('song_list')
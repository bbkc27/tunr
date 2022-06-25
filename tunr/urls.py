from django.urls import path
from . import views

urlpatterns = [
  # path('artists/', views.artist_list, name='artist_list'),
  path('artists/', views.ArtistList.as_view(), name='artist_list'),
  # path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
  path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
  # path('artists/new', views.artist_create, name='artist_create'),
  # path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
  # path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
  # path('songs/', views.song_list, name='song_list'),
  path('songs/', views.SongList.as_view(), name='song_list'),
  # path('songs/<int:pk>', views.song_detail, name='song_detail'),
  path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
  # path('songs/new', views.song_create, name='song_create'),
  # path('songs/<int:pk>/edit', views.song_edit, name='song_edit'),
  # path('songs/<int:pk>/delete', views.song_delete, name='song_delete'),
]
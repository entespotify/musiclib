from rest_framework import viewsets
from tracks.api.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from tracks.models import Artist, Album, Track



class ArtistViewSet(viewsets.ModelViewSet):
   queryset = Artist.objects.all()
   serializer_class = ArtistSerializer
   lookup_field = 'artistName'

class AlbumViewSet(viewsets.ModelViewSet):
   queryset = Album.objects.all()
   serializer_class = AlbumSerializer
   lookup_field = 'album_name'

class TrackViewSet(viewsets.ModelViewSet):
   queryset = Track.objects.all()
   serializer_class = TrackSerializer
   lookup_field = 'title'
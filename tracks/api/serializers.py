from rest_framework import serializers

from tracks.models import Artist, Album, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
       model = Track
       fields = ['album', 'order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['album_name', 'artists', 'tracks']

class ArtistSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True, read_only=True)
    class Meta:
       model = Artist
       fields = ['artistName', 'artistGenre', 'album']


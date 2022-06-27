from django.shortcuts import render
from tracks.models import Track, Album, Artist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

@permission_classes([])
def TracksView(request):
   if request.method == 'GET':
      album = Album.objects.all()
      artist = Artist.objects.all()
      tracks = Track.objects.all()
      try:
         album.count() + artist.count() + tracks.count() > 0
      except (Album.DoesNotExist + Artist.DoesNotExist + Track.DoesNotExist):
         return Response(status=status.HTTP_404_NOT_FOUND)
      return render(request,'tracks.html', {'albums': album})

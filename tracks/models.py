from django.db import models

class Artist(models.Model):
   artistName = models.CharField(max_length=100)
   artistGenre = models.CharField(max_length=10)

class Album(models.Model):
   album_name = models.CharField(max_length=100)
   artists = models.ForeignKey(Artist, related_name='album', on_delete=models.CASCADE)

class Track(models.Model):
   album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
   order = models.IntegerField()
   title = models.CharField(max_length=100)
   duration = models.IntegerField()

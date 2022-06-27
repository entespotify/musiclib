from django.urls import include, path
from rest_framework import routers
from tracks.api.views import ArtistViewSet, AlbumViewSet, TrackViewSet

from . import views


router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'track', TrackViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
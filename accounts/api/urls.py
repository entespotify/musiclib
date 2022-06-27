from django.urls import include, path
from rest_framework import routers
from accounts.api.views import UserViewSet
from .views import UserView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('all/', UserView)
]

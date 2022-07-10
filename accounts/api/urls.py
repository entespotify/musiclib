from django.urls import include, path
from rest_framework import routers
from accounts.api.views import UserViewSet
from .views import UserView
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('all/', UserView),
   path('login/token', obtain_auth_token, name='login')
]

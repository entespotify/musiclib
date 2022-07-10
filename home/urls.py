from django.contrib import admin
from django.urls import path

from .views import homeView, login_view, logout_view, api_login_view

urlpatterns = [
	path('', homeView ),
	path('home/', homeView, name="home" ),
	path('login/', login_view, name="login"),
	path('logout/', logout_view, name="logout"),
	path('api/login/', api_login_view, name="api_login"),
]

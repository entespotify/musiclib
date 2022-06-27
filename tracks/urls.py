from django.urls import path

from .views import TracksView

urlpatterns = [
	path('', TracksView),
	# path('<username>', userView)
]

from django.urls import path

from .views import accountView, userView

urlpatterns = [
	path('', accountView),
	path('<username>', userView)
]

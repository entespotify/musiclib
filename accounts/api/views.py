from django.shortcuts import render
from rest_framework import viewsets
from accounts.api.serializers import UserSerializer
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny



class UserViewSet(viewsets.ModelViewSet):
   permission_classes = (AllowAny,)
   queryset = User.objects.all()
   serializer_class = UserSerializer
   lookup_field = 'username'

@permission_classes([])
def UserView(request):
   if request.method == 'GET':
      users = User.objects.all()
      try:
         users.count() > 0
      except User.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

      serializer = UserSerializer(users, many=True)
      return Response(serializer.data)

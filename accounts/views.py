from django.shortcuts import render
from accounts.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated,])
@authentication_classes([IsAuthenticated,])
def accountView(request):

    users = User.objects.filter()
    if users.count() > 0:
        users = users
    else:
        users = 'No users found'

    return render(request,'account.html', {'users': users})

def userView(request, username):

    users = User.objects.filter(username=username)
    isUser= True
    if users.count() > 0:
        users = users
    else:
        users = User(username='No users found', email= 'Null')

    return render(request,'account.html', {'users': users, 'isUser': isUser})

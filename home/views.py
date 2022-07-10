import email
from django.shortcuts import render, redirect
from .forms import AccountAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.forms import AuthenticationForm

@permission_classes([IsAuthenticated])
def homeView(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "home.html")

def logout_view(request):
	logout(request)
	return redirect("home")

def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "login.html", context)

def api_login_view(request):
    return render(request, "api-login.html")
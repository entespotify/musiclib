from django.shortcuts import render

def homeView(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")

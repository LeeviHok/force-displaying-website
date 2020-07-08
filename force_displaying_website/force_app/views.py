from django.shortcuts import render

def home(request):
    return render(request, 'force_app/home.html')

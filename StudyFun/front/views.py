from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    return render(request, 'front/page_home.html')

def helpPage(request):

    return render(request,'front/page_help.html')

def settingsPage(request):

    return render(request, 'front/page_settings.html')

def statisticsPage(request):
    return render(request, 'front/page_statistics.html')
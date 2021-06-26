from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # Charging last input
    return render(request, 'front/page_home.html')

def helpPage(request):
    # Charging last input
    return render(request, 'front/page_help.html')
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from ...back.models import Keyword_Definition_Dictionary


# Create your views here.
def index(request):
    # Charging last input
    return render(request, 'front/page_home.html')


def helpPage(request):
    # Charging last input
    return render(request,'front/page_help.html')


def settingsPage(request):
    # Charging last input
    result = 2
    return render(request, 'front/page_settings.html', {'result': result})


def add_keyword_definition_to_db(request: HttpRequest):
    keyword_definition_pair = Keyword_Definition_Dictionary(keyword=request.POST["keyword"], definition=request.POST["definition"], difficulty=request.POST["difficulty"])
    keyword_definition_pair.save()
    return redirect("/managestacks/viewstacks")


    return render(request, 'front/page_settings.html')

def statisticsPage(request):
    return render(request, 'front/page_statistics.html')
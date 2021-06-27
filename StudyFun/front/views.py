from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# from ..back import views


# Create your views here.
def index(request):
    # Charging last input
    return render(request, 'front/page_home.html')


def help_page(request):
    # Charging last input
    return render(request, 'front/page_help.html')


def settings_page(request):
    # Charging last input
    return render(request, 'front/page_settings.html')


def manage_stacks_page(request):
    # Charging last input
    # context = {"stacks_list": Keyword_Definition_Dictionary.objects.all()}
    return render(request, 'front/page_managestacks.html')


def add_keyword_definition_to_db(request: HttpRequest):
    keyword_definition_pair = Keyword_Definition_Dictionary(keyword=request.POST["keyword"], definition=request.POST["definition"], difficulty=request.POST["difficulty"])
    keyword_definition_pair.save()
    return redirect("/managestacks/viewstacks")


def statistics_page(request):
    return render(request, 'front/page_statistics.html')

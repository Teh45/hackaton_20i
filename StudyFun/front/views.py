from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Keyword_Definition_Dictionary, Stacks_Database


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
    context = {"stacks_list": Stacks_Database.objects.all()}
    return render(request, 'front/page_managestacks.html', context)


# def insert_stack(request: HttpRequest):
#     keyword_definition_pair = Keyword_Definition_Dictionary(keyword=request.POST["keyword"], definition=request.POST["definition"], difficulty=request.POST["difficulty"])
#     keyword_definition_pair.save()
#     return redirect("/managestacks/viewstacks")


def insert_stack(request: HttpRequest):
    stack = Stacks_Database(name=request.GET["stackName"])
    stack.save()
    return redirect("/front/stacks/")


def delete_stack(request, stack_id):
    stack_to_delete = Stacks_Database.objects.get(id=stack_id)
    stack_to_delete.delete()
    return redirect("/front/stacks/")


def statistics_page(request):
    return render(request, 'front/page_statistics.html')

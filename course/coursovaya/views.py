from http.server import HTTPServer
from idlelib.mainmenu import menudefs

from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def index_whit_authorization(request):
    return render(request, "index_whit_authorization.html")

def authorization(request):
    return  render(request, "authorization.html")

def clas(request):
    return  render(request, "class.html")

def constructor(request):
    return  render(request, "constructor.html")

def history(request):
    return  render(request, "history.html")

def index(request):
    return  render(request, "index.html")

def modernrobot(request):
    return  render(request, "modernrobot.html")

def robototex(request):
    return  render(request, "robototex.html")

def entrance(request):
    return  render(request, "entrance.html")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

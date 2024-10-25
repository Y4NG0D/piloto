from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>A view funcionou!!! Wooow quee legaaal!</h1>")

def sobre(request):
    return HttpResponse("<h2>Sistema 1.0 desenvolvido por mim mesmo!</h2>")

def contato(request):
    return HttpResponse("<h2>Esta é a página de contato do nosso site!</h2>")

def ajuda(request):
    return HttpResponse("<h2>Esta é a página de ajuda do nosso site!</h2>")
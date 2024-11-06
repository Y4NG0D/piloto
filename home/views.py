from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return HttpResponse("<h2>Sistema 1.0 desenvolvido por mim mesmo!</h2>")

def contato(request):
    return HttpResponse("<h2>Esta é a página de contato do nosso site!</h2>")

def home(request):
    return HttpResponse("<h2>Esta é a página de home do nosso site!</h2>")

#view exibir_item
def exibir_item(request, id):
    return render(request, "exibir_item.html, {'id':id}")

def perfil(request, usuario):
    context = {
        'usuario': usuario
    }
    return render()
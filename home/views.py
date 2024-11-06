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
    return render(request, "exibir_item.html", {'id':id})

def perfil(request, usuario):
    context = {
        'usuario': usuario
    }
    return render(request, 'perfil.html', context)

def diasemana(request, numero):
    # definir os dias da semana
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    
    # se n tiver de 1 a 7 da erro, se tiver funciona
    dia = dias_semana.get(numero)
    if dia:
        context = {'numero': numero, 'dia': dia}
        return render(request, 'diasemana.html', context)
    else:
        return HttpResponse("Número inválido! Digite um número de 1 a 7.")
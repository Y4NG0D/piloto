from django.shortcuts import render

from .forms import ContatoForm, ProdutoForm

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def forms(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produto/forms.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)


#view exibir_item
def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id':id})

def produtos(request):
    contexto = {
        'lista': [
            {'id':1, 'nome':'Notebook', 'preco':'2.500,00'},
            {'id':2, 'nome':'Monitor', 'preco':'500,00'},
            {'id':3, 'nome':'Teclado', 'preco':'80,00'},
        ],
    }
    return render(request, 'produto/lista.html', contexto)

def detalhes_produto(request, id):
    return render(request, 'produto/detalhes.html', {'item':id})

def editar_produto(request, id):
    form = ProdutoForm()
    contexto = {
        'form': form,
        'item': id,
    }
    return render(request, 'produto/forms.html', contexto)

def excluir_produto(request, id):
    return render(request, 'produto/excluir.html', {'item':id})

def perfil(request, usuario):
    context = {
        'usuario': usuario
    }
    return render(request, 'perfil.html', context)

def diasemana(request,dia):
    dia_semana = ""
    if dia == 1:
        dia_semana = 'Domingo'
    elif dia == 2:
        dia_semana = 'Segunda-Feira'
    elif dia == 3:     
        dia_semana = 'Terça-Feira'
    elif dia == 4:
        dia_semana = 'Quarta-Feira'
    elif dia == 5:  
        dia_semana = 'Quinta-Feira'
    elif dia == 6:  
        dia_semana = 'Sexta-Feira'
    elif dia == 7:  
        dia_semana = 'Sábado'
    else:  
        dia_semana = 'Inválido' 
    
    return render(request, "diasemana.html", {'num':dia, 'dia':dia_semana})

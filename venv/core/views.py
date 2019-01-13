from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista
from .forms import (
    PessoaForm, VeiculoForm, MovRotativoForm,
    MensalistaForm, MovMensalistaForm)

def home(request):
    context = {'mensagem' : 'Ola Mundo'}
    return render(request, 'core/index.html', context)
#CRUD Pessoa
def pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    dados = {'pessoas' : pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', dados)

def nova_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_listaPessoas')

def update_pessoa(request, id):
    dados = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    dados['pessoa'] = pessoa
    dados['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_listaPessoas')
    else:
        return render(request, 'core/update_pessoa.html', dados)
    
#CRUD Veiculos
def veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    dados = {'veiculos' : veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', dados)

def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_listaVeiculos')

#CRUD Movimento Rotativo
def movRotativo(request):
    movRotativo = MovRotativo.objects.all()
    form = MovRotativoForm()
    dados = {'movRotativo' : movRotativo, 'form': form}
    return render(request, 'core/lista_movRotativo.html', dados)

def novo_movRotativo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_listaMovRotativo')

#CRUD Mensalistas
def mensalista(request):
    mensalista = Mensalista.objects.all()
    form = MensalistaForm()
    dados = {'mensalista' : mensalista, 'form' : form}
    return render(request, 'core/lista_mensalista.html', dados)

def novo_mensalista(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_listaMensalista')

#CRUD Movimento Mensalistas
def movMensalista(request):
    movMensalista = MovMensalista.objects.all()
    form = MovMensalistaForm()
    dados = {'movMensalista' : movMensalista, 'form': form}
    return render(request, 'core/lista_movMensalista.html', dados)

def novo_movMensalista(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_listaMovMensalista')
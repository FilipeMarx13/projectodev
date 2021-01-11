from django.shortcuts import render, redirect
from core.models import cadastro_pessoa
import requests

# Create your views here.

def lista_pessoas(request):
    cadastropessoas = cadastro_pessoa.objects.all()
    dados = {'cadastropessoas': cadastropessoas}
    return render(request, "cadastraopessoas.html", dados)


def novocadastro(request):
    id_pessoa = request.GET.get('id')
    dados = {}
    if id_pessoa:
       dados['cadastro_pessoa'] = cadastro_pessoa.objects.get(id=id_pessoa)
    else:
        response = requests.get("https://gerador-nomes.herokuapp.com/nome/aleatorio")
        json = response.json()
        pessoa = cadastro_pessoa()
        pessoa.nome = json[0]
        pessoa.sobrenome = json[1] + ' ' + json[2]
        pessoa.idade = None
        dados['cadastro_pessoa'] = pessoa

    return render(request, 'novocadastro.html', dados)


def submit_novocadastro(request):
    if request.POST:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        idade = request.POST.get('idade')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        apelido = request.POST.get('apelido')
        observacao = request.POST.get('observacao')
        id_pessoa = request.POST.get('id_pessoa')        
        if id_pessoa:
            cadastro_pessoa.objects.filter(id=id_pessoa).update(nome=nome,
                                                                sobrenome=sobrenome,
                                                                idade=idade,
                                                                data_nascimento=data_nascimento,
                                                                email=email,
                                                                apelido=apelido,
                                                                observacao=observacao)

        else:
            cadastro_pessoa.objects.create(nome=nome,
                                           sobrenome=sobrenome,
                                           idade=idade,
                                           data_nascimento=data_nascimento,
                                           email=email,
                                           apelido=apelido,
                                           observacao=observacao)
    return redirect('/')

def delete_cadastro(request, id_pessoa):
    cadastro_pessoa.objects.filter(id=id_pessoa).delete()
    return redirect('/')

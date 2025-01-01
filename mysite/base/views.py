from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from mysite.base.forms import RegistroUsuarioForm, TarefaForm, TarefaNovaForm
from mysite.base.models import Tarefa


def logged_out(request):
    return render(request, 'registration/logged_out.html')


def registrar_usuario(request):
    """View para registrar novos usuários"""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após o registro
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('base:home')
        else:
            messages.error(request, 'Erro ao realizar o cadastro. Verifique os dados fornecidos.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registrar_usuario.html', {'form': form})


@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:home'))
    else:
        form = TarefaNovaForm()  # Garante que o formulário está disponível no GET

    tarefa_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()

    # Adicionar paginação
    pendentes_paginator = Paginator(tarefa_pendentes, 5)  # 5 tarefas por página
    feitas_paginator = Paginator(tarefas_feitas, 5)

    # Pegamos a página atual via GET
    pendentes_page = request.GET.get('pendentes_page', 1)
    feitas_page = request.GET.get('feitas_page', 1)

    # Paginar os resultados
    tarefa_pendentes = pendentes_paginator.get_page(pendentes_page)
    tarefas_feitas = feitas_paginator.get_page(feitas_page)

    return render(
        request,
        'base/home.html',
        {
            'tarefa_pendentes': tarefa_pendentes,
            'tarefas_feitas': tarefas_feitas,
        },
    )


@login_required
def detalhe(request, tarefa_id):
    # Busca a tarefa ou retorna erro 404 se não encontrada
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        # Cria o formulário associado à tarefa com os dados enviados
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            # Salva as alterações caso o formulário seja válido
            form.save()
            # Redireciona para a página inicial com as alterações salvas
            return HttpResponseRedirect(reverse('base:home'))
    else:
        # Para requisição GET, mostra o formulário com os dados da tarefa
        form = TarefaForm(instance=tarefa)

    # Renderiza a página de detalhe/edição com o formulário e os dados da tarefa
    return render(request, 'base/detalhe.html', {'form': form, 'tarefa': tarefa})


@login_required
def apagar(request, tarefa_id):
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa, id=tarefa_id)
        tarefa.delete()
    return HttpResponseRedirect(reverse('base:home'))

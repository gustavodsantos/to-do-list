from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from mysite.base.forms import RegistroUsuarioForm, TarefaNovaForm
from mysite.base.models import Tarefa


def logged_out(request):
    return render(request, 'registration/logged_out.html')


# View para registrar um novo usuário
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após registro
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect(reverse('base:home'))
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registrar_usuario.html', {'form': form})


# Página inicial com listagem e gerenciamento de tarefas
@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return HttpResponseRedirect(reverse('base:home'))
    else:
        form = TarefaNovaForm()

    # Listar tarefas com paginação
    tarefas_pendentes = Tarefa.objects.filter(feita=False).order_by('-criada_em')
    tarefas_feitas = Tarefa.objects.filter(feita=True).order_by('-criada_em')

    pendentes_paginator = Paginator(tarefas_pendentes, 5)
    feitas_paginator = Paginator(tarefas_feitas, 5)

    pendentes_page = request.GET.get('pendentes_page', 1)
    feitas_page = request.GET.get('feitas_page', 1)

    tarefas_pendentes = pendentes_paginator.get_page(pendentes_page)
    tarefas_feitas = feitas_paginator.get_page(feitas_page)

    return render(
        request,
        'base/home.html',
        {
            'tarefas_pendentes': tarefas_pendentes,
            'tarefas_feitas': tarefas_feitas,
            'form': form,  # Form para adicionar novas tarefas
        },
    )


# Marcar tarefa como feita
@login_required
def marcar_como_feita(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.feita = True
        tarefa.save()
        messages.success(request, f'Tarefa "{tarefa.nome}" marcada como concluída!')
    return HttpResponseRedirect(reverse('base:home'))


# Marcar tarefa como pendente novamente
@login_required
def marcar_como_pendente(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.feita = False
        tarefa.save()
        messages.success(request, f'Tarefa "{tarefa.nome}" marcada como pendente!')
    return HttpResponseRedirect(reverse('base:home'))


# Apagar tarefa
@login_required
def apagar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, f'Tarefa "{tarefa.nome}" foi apagada com sucesso.')
    return HttpResponseRedirect(reverse('base:home'))

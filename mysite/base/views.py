from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mysite.base.forms import TarefaForm, TarefaNovaForm
from mysite.base.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:home'))
        else:
            tarefa_pendentes = Tarefa.objects.filter(feita=False).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            return render(
                request,
                'base/home.html',
                {
                    'form': form,
                    'tarefa_pendentes': tarefa_pendentes,
                    'tarefas_feitas': tarefas_feitas,
                },
                status=400,
            )
    tarefa_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    return render(
        request,
        'base/home.html',
        {
            'tarefa_pendentes': tarefa_pendentes,
            'tarefas_feitas': tarefas_feitas,
        },
    )


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('base:home'))


def apagar(request, tarefa_id):
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('base:home'))

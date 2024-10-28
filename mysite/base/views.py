from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mysite.base.forms import TarefaNovaForm
from mysite.base.models import Tarefa


def home(request):
    if request.method == 'POST':

        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:home'))
        else:
            tarefa_pendentes = Tarefa.objects.filter(feita=False).all()
            return render(request, 'base/home.html', {'form': form, 'tarefa_pendentes': tarefa_pendentes}, status=400)
    tarefa_pendentes = Tarefa.objects.filter(feita=False).all()
    return render(request, 'base/home.html', {'tarefa_pendentes': tarefa_pendentes})

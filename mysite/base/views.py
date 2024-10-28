from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mysite.base.forms import TarefaNovaForm


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('base:home'))
        else:
            return render(request, 'base/home.html', {'form': form}, status=400)
    return render(request, 'base/home.html')

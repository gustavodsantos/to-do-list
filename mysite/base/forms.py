from django.forms import ModelForm

from mysite.base.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']

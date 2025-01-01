from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from mysite.base.models import Tarefa, User


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.strip() == '':
            raise ValidationError('O nome da tarefa não pode ser vazio ou só conter espaços.')
        return nome


class RegistroUsuarioForm(UserCreationForm):
    """Formulário para cadastro de usuários"""

    nome = forms.CharField(max_length=64, label='Nome')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'nome']

    def save(self, commit=True):
        user = super().save(commit=False)
        nome = self.cleaned_data['nome']

        user.first_name = nome
        if commit:
            user.save()
        return user

from django.core.exceptions import ValidationError
from django.db import models
from django_min_custom_user.models import MinAbstractUser


class User(MinAbstractUser):
    pass


class Tarefa(models.Model):
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)

    def clean(self):
        # Validações adicionais
        if not self.nome.strip():
            raise ValidationError('O campo nome não pode ser apenas espaços.')

    def save(self, *args, **kwargs):
        # Garante que o método clean seja executado antes de salvar
        self.clean()
        super().save(*args, **kwargs)

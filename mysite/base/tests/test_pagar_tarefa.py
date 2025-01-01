# import pytest
# from django.urls import reverse
#
# from mysite.base.models import Tarefa
#
#
# @pytest.fixture
# def tarefa(db):
#     return Tarefa.objects.create(nome='Tarefa 1', feita=True)
#
#
# @pytest.fixture
# def resposta(client, tarefa):
#     resp = client.post(
#         reverse('base:apagar', kwargs={'tarefa_id': tarefa.id}),
#     )
#     return resp
#
#
# def test_apagar_tarefa(resposta):
#     assert not Tarefa.objects.exists()

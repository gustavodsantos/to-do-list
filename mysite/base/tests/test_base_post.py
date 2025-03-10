# import pytest
# from django.urls import reverse
#
# from mysite.base.models import Tarefa
#
#
# @pytest.fixture
# def resposta(client, db):
#     resp = client.post(reverse('base:home'), data={'nome': 'Tarefa'})
#     return resp
#
#
# def test_tarefa_existe_no_bd(resposta):
#     assert Tarefa.objects.exists()
#
#
# def test_redirecionamento_depois_do_salvamento(resposta):
#     assert resposta.status_code == 302
#
#
# @pytest.fixture
# def resposta_resposta_dado_invalido(client, db):
#     resp = client.post(reverse('base:home'), data={'nome': ''})
#     return resp
#
#
# def test_tarefa_nao_existe_no_bd(resposta_resposta_dado_invalido):
#     assert not Tarefa.objects.exists()
#
#
# def test_pagina_com_dados_invalidos(resposta_resposta_dado_invalido):
#     assert resposta_resposta_dado_invalido.status_code == 400

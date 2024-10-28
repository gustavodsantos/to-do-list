import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def resposta(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_formulario_presente(resposta):
    assertContains(resposta, '<form method="POST"')


def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')

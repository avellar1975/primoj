"""Testes para as funções."""
from primoj.funcoes import primos_divisores, verifica_primo, lista_primos_ate
import pytest


def test_primos_divisores():
    esperado = [2, 3]
    resultado = primos_divisores(10)
    assert resultado == esperado


@pytest.mark.parametrize(
    'numeroj_p',
    [13, 17, 97, 101]
)
def test_verifica_primo_verdadeiro(numeroj_p):
    verdadeiro = verifica_primo(numeroj_p)
    assert verdadeiro is True


@pytest.mark.parametrize(
    'numeroj_n',
    [4, 16, 98, 102]
)
def test_verifica_primo_falso(numeroj_n):
    falso = verifica_primo(numeroj_n)
    assert falso is False


def test_lista_primos_ate():
    lista = lista_primos_ate(30)
    resultado = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert lista == resultado

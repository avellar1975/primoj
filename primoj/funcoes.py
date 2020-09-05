"""Relação de Funcoes a serem testadas."""
from math import sqrt


# Crivo de Eratóstenes
def primos_divisores(numero):
    base = int(sqrt(numero) + 1)
    divisores = [2]

    for inteiro in range(2, base):
        contador = 0
        for div in divisores:
            if inteiro % div == 0:
                contador += 1
        if contador == 0:
            divisores.append(inteiro)
    return divisores


def verifica_primo(inteiro):
    divisores = primos_divisores(inteiro)
    cont = 0
    for div in divisores:
        if inteiro % div == 0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False


def lista_primos_ate(limite):
    lista = [2]
    for i in range(2, limite):
        if verifica_primo(i):
            lista.append(i)
    return lista

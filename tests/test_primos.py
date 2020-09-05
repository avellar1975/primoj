from primoj.funcoes import primos_divisores, verifica_primo, lista_primos_ate

def test_primos_divisores():
    esperado = [2, 3]
    resultado = primos_divisores(10)
    assert resultado == esperado

def test_verifica_primo():
    falso = verifica_primo(9)
    verdadeiro = verifica_primo(17)
    assert falso == False
    assert verdadeiro == True

def test_lista_primos_ate():
    lista = lista_primos_ate(30)
    resultado = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert lista == resultado

[![Build Status](https://travis-ci.org/avellar1975/primoj.svg?branch=master)](https://travis-ci.org/avellar1975/primoj)
[![Updates](https://pyup.io/repos/github/avellar1975/primoj/shield.svg)](https://pyup.io/repos/github/avellar1975/primoj/)
[![Python 3](https://pyup.io/repos/github/avellar1975/primoj/python-3-shield.svg)](https://pyup.io/repos/github/avellar1975/primoj/)

# primoj

Essa biblioteca é conceitual para mostrar como se cria passo-a-passo uma biblioteca para publicação no Pypi, com integração contínua utilizando o travis ci.

## O que faz essa biblioteca

**primoj** (primos em esperanto) trabalhar com 3 funções para utilizar em números primos.

## Funções
* `primos_divisores(numero)` - Recebe número inteiro e retorna divisores primos que serão utilizados para verificar se o número é divisível por algum deles. Utilizando o Crivo de Eratóstenes.


* `verifica_primo(numero)` - Recebe número inteiro e retorna True para número primo ou False para número não primo.

* ` lista_primos_ate(limite)` - Recebe número inteiro e retorna todos os primos até o número informado no formato de lista.

# Criação de biblioteca

## Criar projeto no git
Criar repositório no GitHub com README, LICENCE e gitignore

## Clonar o repositório recém criado
git clone git@github.com:avellar1975/primoj.git

## Criar a estrutura do projeto
```
Pasta nome do projeto
	- Arquivo py com o projeto
	__init__.py

Pasta tests
	- Arquivo test_nome.py
	__init__.py
.gitignore
LICENCE
README.md
setup.py
```
A utilização do __init__ dentro das pastas do projeto e teste fazem com que consigamos importar os módulos com mais facilidade <kbd>from modulo import funcao</kbd>, por exemplo. E também facilita a execução do pytest no diretório e teste.

O arquivo LICENCE gerado quando criamos o reposítório, será utilizado pelo Pypi.

## Trabalhar com venv
python -m venv .venv
source .venv/bin/activate

## Instalar o flake8
pip install flake8

## Gerar o requirements-dev.txt
### Ambiente de desenvolvimento:
pip freeze > requirements-dev.txt

### Dependencias de produção
requirements.txt

## Configurar o arquivo .traves.yml
```
language: python
python:
  - 3.8
install:
  - pip install -q -r requirements-dev.txt
script:
  - flake8 primoj/funcoes.py
  - pytest -v
```

## Vincular o repositório no travis ci

## Upgrade de Dependências
https://pyup.io/
Adicionar repositório


## Construir o arquivo setup.py

## Empacotando nosso projeto
python setup.py sdist (cria um diretório com a distribuição)

## Criar conta no Pypi

### Definindo padrões de opção no setup.cfg
Para essa questão, temos o arquivo setup.cfg. Nele, podemos definir algumas opções padrões para o setup do projeto. No nosso caso, precisamos especificar a localização do README e do LICENSE, dessa forma:

```
[metadata]
description-file = README.md
license_file = LICENSE
```
### Criar o arquivo de setup.py

## Fazendo o upload de nosso projeto no PyPI

pip install twine
twine upload dist/* (ou uma versão específica pacote-01.zip)
Credenciais do Pypi
pip install nomedopacote

## Futuro
Para criar uma nova versão:
Atualizar a versão no __init__
Configurar versão no __init__ com o conteudo:
__version__ = '0.4'

Covcod e Pyup

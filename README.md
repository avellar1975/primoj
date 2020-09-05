[![Build Status](https://travis-ci.org/avellar1975/primoj.svg?branch=master)](https://travis-ci.org/avellar1975/primoj)

# primoj

Criação passo-a-passo de uma biblioteca para publicação no Pypi, com integração contínua utilizando o travis ci.

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


Configurar versão no __init__ com o conteudo:
__version__ = '0.4'

Construir o arquivo setup.py
- Precisa do long_description=README.md e do licence=read(LICENSE)

Criar o MANIFEST.in com o conteúdo:
include README.md
include LICENSE



Trabalhar com branches e pull request

Covcod e Pyup

Criar conta no Pypi

python setup.py sdist (cria um diretório com a distribuição)

pip install twine
twine upload dist/* (ou uma versão específica pacote-01.zip)
Credenciais do Pypi

pip install nomedopacote

Para criar uma nova versão:
Atualizar a versão no __init__
python setup.py sdist (cria uma nova distribuição)
twine upload dist/*

estrutura:
```
----projeto
|   |--projeto.py
|   |-- __init__.py
|
|LICENCE
|README.md
|setup.py
|MANIFEST.in
```

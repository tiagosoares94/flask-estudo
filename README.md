# Sistema de Coleta de Dados Epidemiológicos

Projeto a ser desenvolvido pela disciplina Laboratório de Engenharia de Software, ministrada pelo professor Fabrício Galende, na Fatec São José dos Campos.

___

## Feito com

* Python 3.7
* Flask 1.1.2
* Gunicorn 20.0.4
* SQLAlchemy 1.3.19
* Jinja 2.11.2

## Configuração

1. Clone o repositório;

2. Configuração de Ambiente
    * python3 -m venv env
    * source env/bin/activate
    * pip3 install --upgrade pip
    * pip3 install -r requirements.txt

3. Execute o Gunicorn
    * gunicorn --bind 0.0.0.0:5000 wsgi:app
    * Acesse: http://0.0.0.0:5000

4. Vídeo de configuração do ambiente:
https://www.youtube.com/watch?v=CpF3OYOCMPo
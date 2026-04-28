# ESTUDO DO DJANGO 2026 

## Preparação do ambiente
- Após subir um venv
- 'pip install update'
- 'python.exe -m pip install --upgrade pip'
- 'pip install Django'

## CMD's do DJANGO

- **'django-admin starproject "NOME DO PROJETO" .'** - para criar um projeto, sendo que o "." após o nome serve para ajudar a fazer deploy do projeto depois de pronto.

- **'django-admin --version'** - para validar a versão.
- **'python manage.py migrate'** - para implementar o BD no projeto, ele olhará para o BD que está definido no settings.py na pasta dentro do projeto.
- **'python manage.py runserver'** - inicia projeto.

## Sequências de ações para montar o projeto
1. 'django-admin --version'
2. 'django-admin starproject "NOME DO PROJETO" .'
3. 'python manage.py migrate'
4. 'python manage.py runserver'

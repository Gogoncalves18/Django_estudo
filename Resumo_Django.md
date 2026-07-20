# ESTUDO DO DJANGO 2026 

## Preparação do ambiente
- Após subir um venv
- 'pip install update'
- 'python.exe -m pip install --upgrade pip'
- 'pip install Django'

## CMD's do DJANGO

- **'python manage.py createsuperuser'** - cria um user no adm do BD.
- **'django-admin startproject "NOME DO PROJETO" .'** - para criar um projeto, sendo que o "." após o nome serve para ajudar a fazer deploy do projeto depois de pronto.
- **'django-admin --version'** - para validar a versão.
- **'python manage.py migrate'** - para implementar o BD no projeto, ele olhará para o BD que está definido no settings.py na pasta dentro do projeto.
- **'python manage.py runserver'** - inicia projeto.
- **'python manage.py makemigrations "NOME DO APP"'** - faz a atualiação no BD da estrutura que foi criada em models.py para o BD. Cada app tem sua estrutura de BD.
- **'python manage.py migrate'** - faz a atualização do BD após definir ou atualizar uma estrutura no BD.
- **'python manage.py startapp "NOME DO APP"'** -cmd para criar o corpo de cada modulo do projeto. Ela precisa ser no mesmo nivel que o manage.py.

## Sequências de ações para montar o projeto
1. 'django-admin --version'
2. 'django-admin starproject "NOME DO PROJETO" .'
3. 'python manage.py migrate'
4. 'python manage.py runserver'
5. 'python manage.py startapp "NOME DO APP"'
6. necessário colocar o nome do app em 'settings.py' dentro de 'INSTALLED_APPS = [...]'
7. Crio a estrutura do BD em 'models.py'
8. 'python manage.py makemigrations "NOME DO APP"'
9. 'python manage.py migrate'
10. 'python manage.py createsuperuser'
11. colocar dentro do admin.py dentro do app, o models criado para apresentar no painel adm.
12. Ajustar as rotas em urls.py
13. Cuidar dos nomes dentro das rotas da url que irá apontar para as views
14. Rodar 'pip install django-bootstrap5' para ele instalar a versao 5 do bootstrap

## Fluxo dos parametros, urls e views
1. No html podemos preparar um href que nos levará para um link que pode ter um ID ou qq
outra infos.
2. Este link se tiver mapeado nas urls acionará a view, entregando para ela request e parametro.
3. Dentro da view eu faço o processamento e atualizo o front respondendo o request.
 
## Cuidados:
### Quando ocorre de atualizar novos campos nas tab dentro do banco. Neste caso eu precisei colocar um ID de user dentro de cada registro de topicos para que cada tópico tenha um dono:
1. *'python manage.py makemigrations lista_tarefas'* - ele prepara a seq de cmds para atualizar a tab. Como eu tenho tanto a tab de Topicos populada e a de User, ele não sabe qual ID de user usar para cada reg. Por isto ele pergunta se quero colocar um valor padrão ou preencher manualmente, nesta sequencia. Escolhi por colocar vlr padrão. Depois ele pedirá o valor, por exemplo, coloquei o valor 2, que é o id de GOG. Cmd tem como ultimo 'arg=nome_app'.
2. *'python manage.py migrate'* - este executa a atualização na tab.

## PAREI NA AULA 10 - no inicio
https://www.youtube.com/watch?v=BA1tGaFmbv0&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=15

necessario ver sobre o crispy


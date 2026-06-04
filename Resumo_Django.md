# ESTUDO DO DJANGO 2026 

## Preparação do ambiente
- Após subir um venv
- 'pip install update'
- 'python.exe -m pip install --upgrade pip'
- 'pip install Django'

## CMD's do DJANGO

- **'python manage.py createsuperuser'** - cria um user no adm do BD.
- **'django-admin starproject "NOME DO PROJETO" .'** - para criar um projeto, sendo que o "." após o nome serve para ajudar a fazer deploy do projeto depois de pronto.
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
 

## PAREI NA AULA 16 - no inicio
https://www.youtube.com/watch?v=Wjre41OFNhs&list=PLLVddSbilcumgeyk0z6ko5U_FYPfbRO2C&index=17


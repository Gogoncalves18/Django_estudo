from django.db import models
# Importo o "User" de ambiente de controle de auth
# para conectar ele a tab Topicos onde cada topico
# terá uma coluna de dono "owner"
from django.contrib.auth.models import User


class Topicos(models.Model):
    """Titulos das tarefas"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    # Definicao de um vinculo dos registro na tab topicos
    # com o id que é dono dela. Quando faço a modificação em
    # uma tab que já está populada, eu preciso fazer o
    # "makemigrations" e o "migrate".
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Mostra o como será mostrado os dados no ADM"""
        # Mostra somente o campo text da tabela
        return self.text


class Sub_topicos(models.Model):
    """ Estrutura de subtopicos dentro de uma tarefa """

    # Esta funcao serve para ligar a PK de Topicos e se ela for deletada,
    # ele deleta todos os subtopicos da tabela ligada a ela.
    sub_topicos = models.ForeignKey(Topicos, on_delete=models.CASCADE)

    # Função para definir que o campo é para texto longo.
    text_sub_topicos = models.TextField()

    # Função para preencher automaticamente data do registro quando atualizado.
    date_added = models.DateTimeField(auto_now_add=True)

    # Class especial do Django para tratar nas as palavras em plural
    # na tab adm.
    class Meta:
        verbose_name_plural = 'sub_topicos_s'

    def __str__(self):
        """ Mostra o como será mostrado os dados no ADM"""
        # Mostra somente o campo text da tabela
        return self.text_sub_topicos[:50] + '...'

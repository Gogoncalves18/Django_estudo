from django.db import models

# Create your models here.

# Nova tabela para lista de tarefas principais
class Topicos(models.Model):
    """Titulos das tarefas"""
    # Cria campo texto com tamanho de 200 caracteres
    text = models.CharField(max_length=200)
    # Função para preencher automaticamente data do registro
    date_added = models.DateTimeField(auto_now=True)

    # Função para ajustar o como será mostrado no BD as infos no painel ADM

    def __str__(self):
        """ Mostra o como será mostrado os dados no ADM"""
        # Mostra somente o campo text da tabela
        return self.text


class Sub_topicos(models.Model):
    """ Estrutura de subtopicos dentro de uma tarefa """

    # Esta funcao serve para ligar a PK de Topicos e se ela for deletada, ele deleta
    # todos os subtopicos da tabela ligada a ela.
    sub_topicos = models.ForeignKey(Topicos, on_delete=models.CASCADE)

    # Função para definir que o campo é para texto longo.
    text_sub_topicos = models.TextField()

    # Função para preencher automaticamente data do registro quando atualizado.
    date_added = models.DateTimeField(auto_now_add=True)


    # Class especial do Django para tratar nas as palavras em plural na tab adm.
    class Meta:
        verbose_name_plural = 'sub_topicos_s'

    def __str__(self):
        """ Mostra o como será mostrado os dados no ADM"""
        # Mostra somente o campo text da tabela
        return self.text_sub_topicos[:50] + '...'
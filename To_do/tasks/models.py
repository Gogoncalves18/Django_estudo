from django.db import models
# IMPORTACAO DO MODEL DO USER
from django.contrib.auth import get_user_model

class Task(models.Model):

    # Variavel em tupla para o select do done, ele só aceita str
    STATUS = (
        ('doing', 'DOING'),
        ('done', 'DONE'),
    )

    title = models.CharField(max_length=255)
    # este não possui comprimento maximo
    description = models.TextField()

    # Choices é um select do proprio django, ao qual estou passando uma tupla
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

    # CHAVE PARA LIGAR A TASK AO DONO DELA
    # VEJA QUE EU ESTOU ATRELANDO O MODEL DO USER A TAREFA EM SIM COM O GET_USER_MODEL
    # O get_user_model já me traz as infos do user conectando ela a tarefa e o on_delete
    # serve para quando eu deletar o usuário, ele deleta a tarefa
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # Cria data automaticamente quando o registro é criado
    created_at = models.DateTimeField(auto_now_add=True)

    # Cria data automaticamente quando o registro é atualizado
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from django.db import models


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
    # Cria data automaticamente quando o registro é criado
    created_at = models.DateTimeField(auto_now_add=True)

    # Cria data automaticamente quando o registro é atualizado
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

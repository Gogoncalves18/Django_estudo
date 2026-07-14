from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    # o nome da tabela que vou preencher
    class Meta:
        model = Task
        # Os campos que eu quero preencher no form
        fields = ('title', 'description')

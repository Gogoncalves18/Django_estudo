# Estrutura para criar formulários no Django

# Esta classe é necessários importar para usar os forms do django
# que se baseam nas estruturas do model (tabs do BD).
from django import forms

# Aqui preciso usar '.' antes do models para dizer ao django que eu
# quero o model que está dentro do mesmo nível de pasta.
# E importo a estrutura da tab de Topicos do BD, pois vou me basear
# nas infos relacionadas aos tópicos pai.
from .models import Topicos, Sub_topicos


# Classe para o formulário que herda a estrutura de forms do django.
class Topico_Form(forms.ModelForm):
    # Neste caso é necessário usar a class Meta para fazer o django
    # conectar o form com os campos da tab no BD.
    class Meta:
        # A instância 'model' é necessária para o djando entender 
        # que para este form ele precisa olhar para minha TAB Topicos.
        model = Topicos
        
        # 'fields' é uma instância olhada pelo django para ele saber
        # quais serão os campos que eu quero criar o relacionamento do
        # form com a TAB. Neste caso posso usar um fields por campo ou 
        # vários campos para o fields.
        fields = ['text']

        # Labels que eu também na posso mudar o nome, serve para eu dar nome
        # para cada campo, neste caso ele relaciona o nome novo com o label 
        # através de chave/vlr, se eu não quiser label, é só entrar com ' '.
        labels = {'text': ''}


# Formulario para subTopicos
class Sub_topico(forms.ModelForm):
    class Meta:
        model = Sub_topicos
        fields = ['text_sub_topicos']
        labels = {'text_sub_topicos': ''}

        # Widgets serve para definir para o campo do form a caracteristica
        # dele. Neste caso o TEXTAREA é um tipo de form de texto longo e 
        # ela recebe alguns param, entre eles a definição que será um campo
        # texto de 80 colunas. Para ajustar a largura.
        widgets = {'text_sub_topicos': forms.Textarea(attrs={'cols':80})}

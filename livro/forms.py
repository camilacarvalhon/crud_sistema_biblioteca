from django.forms import ModelForm
from livro.models import Livros

# Create the form class.
class LivroForm(ModelForm):
     class Meta:
            model = Livros
            fields = ['nome', 'autor', 'ano']
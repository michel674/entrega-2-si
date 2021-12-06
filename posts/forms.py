from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'data',
            'conteudo',
        ]
        labels = {
            'titulo': 'Título',
            'data': 'Data de Postagem',
            'conteudo': 'Conteudo',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'autor',
            'texto',
            'data',
        ]
        labels = {
            'autor': 'AutorLabel',
            'texto': 'Comentário',
	    'data': 'data',
        }
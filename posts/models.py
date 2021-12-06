from django.db import models
from django.conf import settings



class Post(models.Model):
    titulo = models.CharField(max_length=255)
    data = models.DateTimeField()
    conteudo = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return f'{self.titulo} ({self.data}) \n {self.conteudo} '

class Comment(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    texto = models.CharField(max_length=280)
    data = models.DateTimeField()	
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.texto}" - {self.autor}'


class Category(models.Model):
    nome = models.CharField(max_length=50)
    descrição = models.CharField(max_length=280)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'"{self.nome}" - {self.descrição}'

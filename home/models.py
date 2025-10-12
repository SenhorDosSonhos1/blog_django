from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(default="wow")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.titulo}"
from django.shortcuts import render
from .models import Post

# Create your views here.
def listar_posts(request):
     posts = Post.objects.all()
     return render(request, 'listar_posts.html', context= {
          'posts': posts
     })

def detalhar_post(request, pk):
     post = Post.objects.get(pk = pk)
     return render(request, "detalhar_post.html", context = {
          "post": post
     })

def criar_post(request):
     ...

def editar_post(request):
     ...

def deletar_post(request):
     ...

def adicionar_comentario(request):
     ...
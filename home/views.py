from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse

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
     if request.method == "POST":
          titulo = request.POST.get("titulo")
          descricao = request.POST.get("descricao")

          #Adicionar o autor como o id do usuario logado
          post = Post.objects.create(
          titulo = titulo,
          descricao = descricao)
          
          post.save()
     
     return redirect(reverse("home"))
          
          
     return render(request, 'criar_post.html')

def editar_post(request):
     ...

def deletar_post(request):
     ...

def adicionar_comentario(request):
     ...
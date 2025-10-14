from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_posts, name='home'),
    path('detalhar_post/<int:pk>/', views.detalhar_post, name='detalhar_post'),
    path('criar_post/', views.criar_post, name='criar_post'),
    path('adicionar_comentario/<int:pk>/', views.adicionar_comentario, name='adicionar_comentario')
]

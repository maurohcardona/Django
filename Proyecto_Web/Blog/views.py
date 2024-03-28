from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def blog(request):
    
    posts = Post.objects.all()
    
    return render(request, 'blog.html', {'blogs': posts})

def categorias(request, categoria_id):
    
    categoria = Categoria.objects.get(id = categoria_id)
    
    posts = Post.objects.filter(categorias = categoria)
    
    return render(request, 'categorias.html', {'categoria': categoria, 'blogs': posts})
    
    
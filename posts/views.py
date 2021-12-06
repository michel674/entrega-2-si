from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Post, Comment,Category
from .forms import PostForm,CommentForm



#Views Genéricas
class ListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    #template_name = 'posts/listagem_de_categorias.html'

def DetailView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)


def CreateView(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = Post(**post_form.cleaned_data)
            post.save()
            
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.pk, )))
    else:
        post_form = PostForm()

    context = {'post_form': post_form}
    return render(request, 'posts/create.html', context)



def UpdateView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.titulo = form.cleaned_data['titulo']
            post.data = form.cleaned_data['data']
            post.conteudo = form.cleaned_data['conteudo']
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'titulo': post.titulo,
                'data': post.data,
                'conteudo': post.conteudo
            })

    context = {'post': post, 'form': form}
    return render(request, 'posts/update.html', context)


def DeleteView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_autor = form.cleaned_data['autor']
            comment_texto = form.cleaned_data['texto']
            comment_data  = form.cleaned_data['data']
            comment = Comment(autor=comment_autor,
                            texto=comment_texto,
                            data =  comment_data,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)



class ListCategoryView(generic.ListView):
    model = Category
    template_name = 'posts/listagem_de_categorias.html'

def DetailCategory(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {'category': category}
    return render(request, 'posts/ListagemPostPorCategoria.html', context)

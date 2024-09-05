from django.shortcuts import render
from .models import Article
from django.views.generic import ListView,DetailView,CreateView

class Articles_list(ListView):
    model = Article
    template_name = "index.html"

class Article_detail(DetailView):
    model = Article
    template_name = "article_detail.html"

class Article_CreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = '__all__'

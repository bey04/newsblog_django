from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article

class ArticListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_articles'] = Article.objects.count()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(
            tags__in=self.object.tags.all()
        ).exclude(id=self.object.id).distinct()[:3]
        return context

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title', 'summary', 'body', 'image', 'tags']
    permission_denied_message = 'Only admin users can create articles.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'summary', 'body', 'image', 'tags']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

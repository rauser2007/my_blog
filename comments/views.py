from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Comment
from articles.models import Article


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        article = Article.objects.get(pk=self.kwargs['article_pk'])
        form.instance.article = article
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.article.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'comments/comment_form.html'

    def get_success_url(self):
        artical_pk = self.get_object().article.pk
        return reverse('articles:article-detail', kwargs={'pk': artical_pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

    def get_success_url(self):
        return self.object.article.get_absolute_url()
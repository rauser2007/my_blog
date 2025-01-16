from django.db import models
from django.contrib.auth.models import User
from articles.models import Article
from django.conf import settings

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.user} on {self.article}'
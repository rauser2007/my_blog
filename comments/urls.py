from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('create/<int:article_pk>/', views.CommentCreateView.as_view(), name='comment-create'),  # Додати коментар
    path('update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment-update'),  # Редагувати коментар
    path('delete/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete'),  # Видалити коментар
]

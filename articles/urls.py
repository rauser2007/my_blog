from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),  # Список статей
    path('artical/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),  # Деталі статті
    path('create/artical/', views.ArticleCreateView.as_view(), name='article-create'),  # Створення статті
    path('update/artical/<int:pk>/', views.ArticleUpdateView.as_view(), name='article-update'),  # Редагування статті
    path('delete/artical/<int:pk>/', views.ArticleDeleteView.as_view(), name='article-delete'),  # Видалення статті
]
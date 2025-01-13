from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),  # Список статей
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),  # Деталі статті
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),  # Створення статті
    path('update/<int:pk>/', views.ArticleUpdateView.as_view(), name='article-update'),  # Редагування статті
    path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article-delete'),  # Видалення статті
]
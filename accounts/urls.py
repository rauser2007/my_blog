from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),  # Увійти
    path('signup/', views.SignUpView.as_view(), name='signup'),  # Реєстрація
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='user-profile'),  # Профіль
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Вийти
]

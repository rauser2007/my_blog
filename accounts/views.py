from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from django.urls import reverse_lazy
import logging
from .forms import CustomUserCreationForm

logger = logging.getLogger(__name__)

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Шлях до вашого шаблону
    redirect_authenticated_user = True  # Перенаправлення, якщо користувач вже увійшов
    success_url = reverse_lazy('home')  # Куди перенаправляти після успішного входу

    def form_valid(self, form):
        logger.info(f"User {form.cleaned_data.get('username')} logged in successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"Failed login attempt for user: {form.cleaned_data.get('username')}")
        return super().form_invalid(form)

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class ProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

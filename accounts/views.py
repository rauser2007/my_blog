from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from django.urls import reverse_lazy

class SignUpView(CreateView):
    model = CustomUser
    fields = ['username', 'password', 'email']
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class ProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

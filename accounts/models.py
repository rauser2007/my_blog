from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="Групи, до яких належить користувач.",
        verbose_name="групи"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Спеціальні дозволи для цього користувача.",
        verbose_name="дозволи"
    )

    def __str__(self):
        return self.username
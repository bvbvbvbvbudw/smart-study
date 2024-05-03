from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True
    )
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',
        blank=True
    )

class userRolesManager(models.Manager):
    userPk = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=10)
    def __str__(self):
        return self.role
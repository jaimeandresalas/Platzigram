from django.db import models

# Django


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    is_admin = models.BooleanField(default=False)
    birthday = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

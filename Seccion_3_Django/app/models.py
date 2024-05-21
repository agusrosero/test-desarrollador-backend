from django.db import models
from django.core.validators import validate_email


class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(validators=[validate_email])

    def __str__(self):
        return self.username


class Producto(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

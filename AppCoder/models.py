from django.db import models

# Create your models here.

class Introduccion(models.Model):
    categoria = models.CharField(max_length=50)

    
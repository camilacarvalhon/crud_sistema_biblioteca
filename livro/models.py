from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()

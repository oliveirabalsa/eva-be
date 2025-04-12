from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('TODO', 'A fazer'), ('IN_PROGRESS', 'Em andamento'), ('DONE', 'Concluída')])
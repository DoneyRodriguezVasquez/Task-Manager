from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATE_CHOICES = [
        ('TO_DO', 'TO DO'),
        ('WAITING', 'WAITING'),
        ('IN_PROGRESS', 'IN PROGRESS'),
        ('DONE', 'DONE'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='TO_DO')
    comments = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


        